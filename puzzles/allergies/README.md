# Allergies

Write a program that, given a person's allergy score, can tell them whether or not they're allergic to a given item, and
their full list of allergies.

An allergy test produces a single numeric score which contains the information about all the allergies the person has (
that they were tested for).

The list of items (and their value) that were tested are:

* eggs (1)
* peanuts (2)
* shellfish (4)
* strawberries (8)
* tomatoes (16)
* chocolate (32)
* pollen (64)
* cats (128)

So if Tom is allergic to peanuts and chocolate, he gets a score of 34.

Now, given just that score of 34, your program should be able to say:

- Whether Tom is allergic to any one of those allergens listed above.
- All the allergens Tom is allergic to., sorted alphabetically

Example:

``` python
>>> allergies = Allergies(0)
>>> allergies.is_allergic_to('peanuts')
True
```

``` python
>>> sorted(Allergies(255).lst))
['cats', 'chocolate', 'eggs', 'peanuts', 'pollen', 'shellfish', 'strawberries', 'tomatoes']
```

``` python
>>> Allergies(259).allergies()
["eggs", "peanuts"]
```

You will be provided with a class `Allergies` which will have 2 methods

+ is_allergic_to Checks if Tom is allergic to a particular allergen. Returns True if Tom is allergic, False otherwise

+ allergies Returns a list of what Tom is allergic to. This list must be sorted alphabetically

Must Dos:

Ensure that your function throws a TypeError for invalid inputs such as None, floats, strings, or any data type that is
not an integer.

*Hint: Use Bitwise ANDing*
