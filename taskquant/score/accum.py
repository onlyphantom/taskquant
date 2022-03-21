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


def score_accum(task_path, verbosity=False):
    """
    Create a scoreboard using 'score' attribute of tasks
    """
    tw = TaskWarrior(data_location=task_path)

    completed = tw.tasks.completed()
    total_completed = len(completed)

    if total_completed < 1:
        return warnings.warn(
            f"{textstyle.OKCYAN}A curious case of 0 completed tasks. Check {textstyle.WARNING}{task_path}{textstyle.OKCYAN} to make sure the path to Taskwarrior's .task is set correctly or try to complete some tasks in Taskwarrior!{textstyle.RESET}",
        )

    cl = list()

    for task in completed:
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

    fulldate = {}
    rollingdate = {}
    while startdate <= enddate:
        fulldate.update({startdate: agg_date_dict.get(startdate, 0)})
        startdate += timedelta(days=1)

    accu = 0
    for k, v in fulldate.items():
        accu += v
        rollingdate.update({k: accu})

    combined_l = []
    for key in fulldate.keys():
        combined_l.append([str(key), fulldate[key], rollingdate[key]])

    combined_l_headers = ["Date", "Score", "Cumulative"]
    # f'\033[1m\033[4m{x}\033[0m'
    combined_l_headers = list(
        map(
            lambda x: f"{textstyle.BOLD}{textstyle.UNDERLINE}{textstyle.OKCYAN}{x}{textstyle.RESET}",
            combined_l_headers,
        )
    )

    if "tabulate" in sys.modules:
        print(tabulate(combined_l, headers=combined_l_headers, tablefmt="pretty"))
    else:
        create_table(combined_l, headers=combined_l_headers)

    if verbosity:
        print(
            f"{textstyle.NORDBG2BOLD}Total completed tasks:{textstyle.RESET}{textstyle.OKGREEN} {total_completed}{textstyle.RESET}"
        )
        print(
            f"{textstyle.NORDBG1BOLD}Active dates:{textstyle.RESET}{textstyle.OKGREEN} {len(agg_date)}{textstyle.RESET}"
        )


if __name__ == "__main__":
    score_accum()
