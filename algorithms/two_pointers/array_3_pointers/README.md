# Array 3 Pointers

You are given 3 arrays A, B and C. All 3 of the arrays are sorted.

Find i, j, k such that :

max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.

Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))

**abs(x) is absolute value of x and is implemented in the following manner : **

      if (x < 0) return -x;
      else return x;

```plain
Example :

Input :
A : [1, 4, 10]
B : [2, 15, 20]
C : [10, 12]

Output : 5
With 10 from A, 15 from B and 10 from C. 
```