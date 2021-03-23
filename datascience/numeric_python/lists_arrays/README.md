This is a directory showcasing the difference between Python lists and Numpy(Numerical Python) arrays. Essentially, they are the same, however they are elementary differences that make Numpy very powerful.

A basic example:
```python
from numpy import array

baseball = [12, 46, 489, 46, 5, 312, 31, 2, 3, 12, 31, 3, 13, 1, 31, 3, 13, 13, 1, 31, 313, 1, 31, 189, 4, 4, 31, 564,
            9, 19, 416, 49, 498, 4984, 1984]

print(type(array(baseball)))
<class 'numpy.ndarray'>

print(type(baseball))
<class 'list'>
```
> The 2 types are not similar, but almost the same operations can be performed on them.

Say for example you get the heights of each football player in England. You call the Barclay's Premier League and since you are a major fan and a major stakeholder in Barclays(They don't just send this data to everyone, I tried), they send you the data of 1000 players' heights as a list. Sadly, they are all in inches and you do not use inches, but rather meters. You could use a `for loop` converting each to meters and multiplying by 0.0254. This will work, but it will take quite a while to execute.

``` python
heights = [78,45,70,80,75,84,76,84,71,72,73,84,75,88,79,...]
m = [x * 0.0254 for x in heights]
print(m)
```
> This uses a list comprehension to obtain a new list of the newly converted heights to meters.

NumPy on the other hand makes this process very simple and efficient. You will not have to use a for loop to perform such an operation.

``` python
from numpy import array
heights = [78,45,70,80,75,84,76,84,71,72,73,84,75,88,79,...]

m = array(heights) * 0.0254
print(m)
```
> The output will be the same. NumPy array function simply took in the list of heights and multiplied each to 0.0254. No loop used.

