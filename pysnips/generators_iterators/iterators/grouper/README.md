# Grouper

A simple implementation to demonstrate usage of the iterator library module in python 3.

The `naive_grouper` script is used to demonstrate an inefficient way of handling iteration. To run the script:

```bash
$ /usr/bin/time -f "Memory Used (kB): %M\nUsed Time: (seconds): %U"python naive_grouper.py
Memory used(KB): 11383308
Used Time: (seconds): 20.98
```

> This shows that this script takes up 20 seconds before finishing and uses 11GB to process a range of 100Million

The `better_grouper` script demonstrates the usage of less memory and is faster in handling larger calculations:

```bash
$ /usr/bin/time -f "Memory used(KB): %M\nUsed Time: (seconds): %U" python better_grouper.py
Memory used(KB): 4553416
Used Time: (seconds): 3.69
```

> This uses approximately ~4.5GB of memory and takes 3.69 seconds to complete for a range of 100Million numbers