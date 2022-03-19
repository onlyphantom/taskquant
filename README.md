### TaskQuant
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

### Roadmap
- Argparse to optionally specify a path to your tasks file
- Add terminal-based charts and graphs
- New ways to visualize scores based on tags, projects or other attributes

### Links to Tutorials
- _to be updated_

