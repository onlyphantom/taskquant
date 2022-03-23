from datetime import date, timedelta
import unittest
from unittest.mock import patch

from taskquant.score.accum import (
    score_accum,
    _extract_tasks,
    _task_to_dict,
    _create_full_date,
    _fill_rolling_date,
    _create_combined_table,
    _create_table_auto,
)


def diff_date(date1, date2):
    return abs((date1 - date2).days)


def create_mock_fulldate():
    today = date.today()
    fulldate = {}
    for i in range(0, 10):
        fulldate.update({today: i})
        today += timedelta(days=1)
    return fulldate


class TestAccum(unittest.TestCase):
    def test_invalid_path_warning(self):
        invalid_task_path = "tests/testdata/"

        with self.assertWarns(Warning):
            score_accum(task_path=invalid_task_path)

    def test_extract_tasks(self):
        task_path = "~/vaults/tasks"
        completed = _extract_tasks(task_path)
        self.assertGreater(len(completed), 0)

    def test_task_to_dict(self):
        task_path = "~/vaults/tasks"
        tasks = _extract_tasks(task_path)
        # days_apart = abs((tasks[-1]["end"] - tasks[0]["end"]).days)
        days_apart = diff_date(tasks[-1]["end"], tasks[0]["end"])

        agg_date_dict, _, _ = _task_to_dict(tasks)
        self.assertEqual(len(agg_date_dict), days_apart)

    def test_create_full_date(self):
        task_path = "~/vaults/tasks"
        tasks = _extract_tasks(task_path)
        agg_date_dict, startdate, enddate = _task_to_dict(tasks)
        fulldate = _create_full_date(startdate, enddate, agg_date_dict)

        # expect number of keys to be equal to number of days between start and end date (inclusive, +1)
        expected_n_keys = diff_date(enddate, startdate) + 1
        self.assertEqual(len(fulldate), expected_n_keys)

    def test_fill_rolling_date(self):
        fulldate = create_mock_fulldate()
        rollingdate = _fill_rolling_date(fulldate)

        expected = sum(fulldate.values())
        self.assertEqual(list(rollingdate.values())[-1], expected)

        self.assertEqual(
            list(rollingdate.values())[-2], sum(list(fulldate.values())[:-1])
        )

    def test_create_combined_table(self):
        fulldate = create_mock_fulldate()
        rollingdate = _fill_rolling_date(fulldate)
        combined_l = _create_combined_table(fulldate, rollingdate)

        expected = [str(date.today() + timedelta(days=9)), 9, 45]
        self.assertListEqual(expected, combined_l[-1])

    def test_create_table_auto(self):
        fulldate = create_mock_fulldate()
        rollingdate = _fill_rolling_date(fulldate)
        combined_l = _create_combined_table(fulldate, rollingdate)
        headers = ["Date", "Score", "Cumulative"]

        with patch("builtins.print") as mock_print:
            _create_table_auto(combined_l, headers, False, 9, 9, True)

            import sys

            print(str(mock_print.call_args_list[0]))
            expected_header = "\\t" + "\\t\\t".join(headers) + "\\t"
            mock_print.assert_called_with("call('{}')".format(expected_header))

            print(str(mock_print.call_args_list[10]))
            expected_lastrow = "\\t".join(
                ["", str(date.today() + timedelta(days=9)), "", "9", "", "45", ""]
            )
            mock_print.assert_called_with("call('{}')".format(expected_lastrow))


if __name__ == "__main__":
    unittest.main()
