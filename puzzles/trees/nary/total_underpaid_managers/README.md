# Find total underpaid managers

Find the total number of underpaid manager if an underpaid manager is a manager whose salary is less than the average of
direct & indirect reports

```plain
+ A($100)
  + B(120)
  + C(200)
    + D(60)
```

> Manager A has a salary of 100, but is less than the average of B(120)+C(200)+D(60) = 380 / 3 = 120
> Manager C has a salary of 200, but is more than D. Theefore the count is 1
