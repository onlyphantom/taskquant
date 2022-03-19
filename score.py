#!/usr/bin/env python3
import sys
from datetime import timedelta
from itertools import groupby

from tasklib import TaskWarrior

try:
    from tabulate import tabulate
except ImportError:
    from utils.create_table import create_table

tw = TaskWarrior(data_location="~/vaults/tasks")


def main():
    completed = tw.tasks.completed()
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

    if "tabulate" in sys.modules:
        print(tabulate(combined_l, headers=combined_l_headers, tablefmt="pretty"))
    else:
        create_table(combined_l, headers=combined_l_headers)


if __name__ == "__main__":
    main()
