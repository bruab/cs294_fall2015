---
title: "Implement argparse in throw_err.py"
published: true
morea_id: Refactor.experience1
morea_type: experience
morea_summary: "Clean up my mess"
morea_sort_order: 1
morea_labels:
 - 1-2 hrs
 - 1 pt
 - due Oct 2
---

### Implement argparse in throw_err.py

If you haven't done so already, fork and clone the repository at [https://github.com/cs294-python/errors](https://github.com/cs294-python/errors). This code works fine, but could be cleaner. Use the built in `argparse` library to simplify handling command line arguments. 

There is more than one way to accomplish this. You'll get a point if your code

- Uses argparse
- Still throws errors based on arguments

*NOTE: By those criteria, it is okay if your code requires slightly different arguments than the original version.* For example, it's acceptable to require typing 

`python throw_err.py --assertion` 

as opposed to 

`python throw_err.py assertion`

BTW [here](https://github.com/genomeannotation/GAG/issues/160) is how (and when) I learned about argparse :)

