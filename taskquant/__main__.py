#!/usr/bin/env python3
import argparse

from taskquant.score.accum import score_accum
from taskquant.utils.helpful import dir_path
from taskquant.utils.colors import textstyle

parser = argparse.ArgumentParser(
    description="CLI utility that extends taskwarrior for productivity scoreboard & gamification"
)
parser.add_argument("-p", "--path", type=dir_path, help="path to your .task")
# add verbose flag
parser.add_argument("-v", "--verbose", action="store_true", help="verbose mode")

args = parser.parse_args()


def main():
    score_accum(task_path=args.path or "~/.task", verbosity=args.verbose)

    # if verbose
    if args.verbose:
        print(
            f"{textstyle.NORDBG2BOLD}task_path:{textstyle.RESET}{textstyle.OKGREEN} {args.path}{textstyle.RESET}"
        )


if __name__ == "__main__":
    main()
