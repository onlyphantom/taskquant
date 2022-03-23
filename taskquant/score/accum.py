import sys
import warnings
from datetime import timedelta
from itertools import groupby

from tasklib import TaskWarrior

try:
    from tabulate import tabulate
except ImportError:
    from taskquant.utils.create_table import create_table

from taskquant.utils.colors import textstyle


def _extract_tasks(task_path):
    tw = TaskWarrior(data_location=task_path)
    return tw.tasks.completed()


def _create_table_auto(
    body, headers, verbosity, completed_length, date_length, plain=False
):

    if plain is False and "tabulate" in sys.modules:
        print(tabulate(body, headers=headers, tablefmt="pretty"))
    else:
        from taskquant.utils.create_table import create_table

        create_table(body, headers=headers)

    if verbosity:
        print(
            f"{textstyle.NORDBG2BOLD}Total completed tasks:{textstyle.RESET}{textstyle.OKGREEN} {completed_length}{textstyle.RESET}"
        )
        print(
            f"{textstyle.NORDBG1BOLD}Active dates:{textstyle.RESET}{textstyle.OKGREEN} {date_length}{textstyle.RESET}"
        )


def _task_to_dict(tasks):
    cl = list()

    for task in tasks:
        cl.append(
            (
                task["project"],
                task["end"].date(),
                task["effort"] or "",
                task["score"] or 0,
                task["tags"],
            )
        )

    # sort cl by ["end"] date
    cl_sorted = sorted(cl, key=lambda x: x[1])

    agg_date = [
        [k, sum(v[3] for v in g)] for k, g in groupby(cl_sorted, key=lambda x: x[1])
    ]

    agg_date_dict = dict(agg_date)
    startdate = agg_date[0][0]
    enddate = agg_date[-1][0]
    return agg_date_dict, startdate, enddate


def _create_full_date(startdate, enddate, agg_date_dict):
    fulldate = {}
    while startdate <= enddate:
        fulldate.update({startdate: agg_date_dict.get(startdate, 0)})
        startdate += timedelta(days=1)
    return fulldate


def _fill_rolling_date(fulldate):
    rollingdate = {}
    accu = 0
    for k, v in fulldate.items():
        accu += v
        rollingdate.update({k: accu})

    return rollingdate


def _create_combined_table(fulldate, rollingdate):
    combined_l = []
    for key in fulldate.keys():
        combined_l.append([str(key), fulldate[key], rollingdate[key]])
    return combined_l


def score_accum(task_path, verbosity=False):
    """
    Create a scoreboard using 'score' attribute of tasks
    """
    completed = _extract_tasks(task_path)

    total_completed = len(completed)

    if total_completed < 1:
        return warnings.warn(
            f"{textstyle.OKCYAN}A curious case of 0 completed tasks. Check {textstyle.WARNING}{task_path}{textstyle.OKCYAN} to make sure the path to Taskwarrior's .task is set correctly or try to complete some tasks in Taskwarrior!{textstyle.RESET}",
        )
    else:
        agg_date_dict, startdate, enddate = _task_to_dict(completed)

    fulldate = _create_full_date(startdate, enddate, agg_date_dict)
    rollingdate = _fill_rolling_date(fulldate)

    combined_l = _create_combined_table(fulldate, rollingdate)
    combined_l_headers = list(
        map(
            # f'\033[1m\033[4m{x}\033[0m'
            lambda x: f"{textstyle.BOLD}{textstyle.UNDERLINE}{textstyle.OKCYAN}{x}{textstyle.RESET}",
            ["Date", "Score", "Cumulative"],
        )
    )

    _create_table_auto(
        combined_l,
        combined_l_headers,
        verbosity,
        total_completed,
        len(agg_date_dict),
        False,
    )
    return completed


if __name__ == "__main__":
    score_accum()
