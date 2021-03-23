## Roman Numeral

Given a roman numeral as input, write a function that converts the roman numeral to a number and outputs it.
 Example:
```python 
translateRomanNumeral("LX") # 60
```

When a smaller numeral appears before a larger one, it becomes a subtractive operation. You can assume only one smaller numeral may appear in front of larger one.
Ex:
```python
translateRomanNumeral("IV") # 4
```
You should return `nil` on invalid input.

Write a function to convert from normal numbers to Roman Numerals.

The Romans were a clever bunch. They conquered most of Europe and ruled
it for hundreds of years. They invented concrete and straight roads and
even bikinis. One thing they never discovered though was the number
zero. This made writing and dating extensive histories of their exploits
slightly more challenging, but the system of numbers they came up with
is still in use today. For example the BBC uses Roman numerals to date
their programmes.

The Romans wrote numbers using letters - I, V, X, L, C, D, M. (notice
these letters have lots of straight lines and are hence easy to hack
into stone tablets).

```
 1  => I
10  => X
 7  => VII
```

There is no need to be able to convert numbers larger than about 3000.
(The Romans themselves didn't tend to go any higher)

Wikipedia says: Modern Roman numerals ... are written by expressing each
digit separately starting with the left most digit and skipping any
digit with a value of zero.

To see this in practice, consider the example of 1990.

In Roman numerals 1990 is MCMXC:

1000=M
900=CM
90=XC

2008 is written as MMVIII:

2000=MM
8=VIII

See also: http://www.novaroma.org/via_romana/numbers.html

### Submitting Exercises

Note that, when trying to submit an exercise, make sure the solution is in the `exercism/python/<exerciseName>` directory.

For example, if you're submitting `bob.py` for the Bob exercise, the submit command would be something like `exercism submit <path_to_exercism_dir>/python/bob/bob.py`.


For more detailed information about running tests, code style and linting,
please see the [help page](http://exercism.io/languages/python).

## Source

The Roman Numeral Kata [http://codingdojo.org/cgi-bin/wiki.pl?KataRomanNumerals](http://codingdojo.org/cgi-bin/wiki.pl?KataRomanNumerals)

## Submitting Incomplete Problems
It's possible to submit an incomplete solution so you can see how others have completed the exercise.



