## isograms

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines
whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

```python
is_isogram("Dermatoglyphics" ) == true
is_isogram("aba" ) == false
is_isogram("moOse" ) == false # -- ignore letter case
```

([a-zA-Z]) - A letter which it captures in the first group; then .*? - zero or more characters (the ? denotes as few as
possible); until \1 - it finds a repeat of the first matched character.

Alternatives Loop through each character in word and check the count of each letter, if the letter is greater than 1, it
is not an isogram, else it is w = word.lower()
for chr in w:
if w.count(chr) > 1:
return False return True

OR

Use a set to determine if the length of unique characters are equal to the characters already present, if they are then
it is an isogram, else it is false
