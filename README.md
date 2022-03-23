## TaskQuant
This is a CLI application that helps Taskwarrior users quantify their productivity by tracking the 'score' attribute in their tasks.

`score` is a custom [User Defined Attributes](https://taskwarrior.org/docs/udas.html). You will need to have that configured in your `.taskrc` file. A sample configuration for this attribute would be:

```
uda.score.type=numeric
uda.score.label=Score 🏆 
urgency.uda.score.coefficient=2
```

TaskQuant will then compute the score(s) you have accumulated across the different tasks and return a scoresheet.

TaskQuant **has no external dependencies** except `tasklib`, which is also by [the same organization](https://github.com/GothenburgBitFactory) that developed Taskwarrior. 

It is written entirely in Python, using standard library. It may have optional dependencies, but those are not required and a fallback option will always be used by default. 

For those reasons, TaskQuant is extremely lightweight. As it stands, it's only 6.8kb of code, and should install in under a second.

#### Installation
TaskQuant is available on [pypi](https://pypi.org/project/taskquant/).
```
pip install taskquant
```

### Usage
Install the package and execute:

```bash
tq 
```

- It supports an optional `-p` (`path`) argument to specify the path to your `.task` file. **Especially** helpful if you changed the default location of your `.task` file.
- It supports an optional `-v` (`verbose`) argument to print out additional 
information in its output.

```bash
tq -p ~/vaults/tasks -v 

# outputs:
+------------+-------+------------+
|    Date    | Score | Cumulative |
+------------+-------+------------+
| 2022-03-09 |   0   |     0      |
| 2022-03-10 |   8   |     8      |
| 2022-03-11 |   1   |     9      |
| 2022-03-12 |  43   |     52     |
| 2022-03-13 |   4   |     56     |
| 2022-03-14 |   4   |     60     |
| 2022-03-15 |   7   |     67     |
| 2022-03-16 |   9   |     76     |
| 2022-03-17 |   4   |     80     |
| 2022-03-18 |   4   |     84     |
| 2022-03-19 |   3   |     87     |
| 2022-03-20 |   2   |     89     |
| 2022-03-21 |   5   |     94     |
+------------+-------+------------+
Total completed tasks: 48
Active dates: 13
task_path: /home/samuel/vaults/tasks
```



- To see all optional arguments, use the `-h` (`help`) argument.

```bash
tq -h
```

#### Dependencies
- [tasklib](https://github.com/GothenburgBitFactory/tasklib)
- (Optional) [tabulate](https://github.com/astanin/python-tabulate)

#### Testing
Tests are written in `unittest` and stored in the `tests` directory.

To execute tests without arguments and automatic test discovery:

```bash
python -m unittest 
```

To test a specific test file (`-v` for verbose output):

```bash
python -m unittest -v tests/test_accum.py

test_create_combined_table (tests.test_accum.TestAccum) ... ok
test_create_full_date ... ok
test_create_table_auto (tests.test_accum.TestAccum) ... ok
test_extract_tasks (tests.test_accum.TestAccum) ... ok
test_fill_rolling_date (tests.test_accum.TestAccum) ... ok
test_invalid_path_warning (tests.test_accum.TestAccum) ... ok
test_task_to_dict (tests.test_accum.TestAccum) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.049s

OK


```

### Roadmap
- Argparse to optionally specify a path to your tasks file
- Add terminal-based charts and graphs
- New ways to visualize scores based on tags, projects or other attributes

### Links to Tutorials
- _to be updated_

