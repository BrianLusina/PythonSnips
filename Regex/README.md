# Regex

These are a series of Regular Expression programs showing how regular expressions can be used to solve particular problems

## Word Count

Kate likes to count words in text blocks. By words she means continuous sequences of alphabetic characters. Here are examples:

Hello there, little user5453 374 ())$. I’d been using my sphere as a stool. Slow-moving target 839342 was hit by OMGd-63 or K4mp. contains "words" ['Hello', 'there', 'little', 'user', 'I', 'd', 'been', 'using', 'my','sphere', 'as', 'a', 'stool', 'Slow', 'moving', 'target', 'was', 'hit', 'by', 'OMGd', 'or', 'K', 'mp']

Kate doesn't like some of words and doesn't count them. Words to be excluded are "a", "the", "on", "at", "of", "upon", "in" and "as", case-insensitive.

Today Kate's too lazy and have decided to teach her computer to count "words" for her.

Example Input 1

Hello there, little user5453 374 ())$.

Example Output 1

4

Example Input 2

I’d been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I’d been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything.

Example Output 2

112

## Pete Talk

Write a function that should take its not always "clean" speech and cover as much as possible of it, in order not to offend some more sensible spirits.

For example, given an input like
```python
What the hell am I doing here? And where is my wallet? PETE SMASH!
```
You are expected to turn it into something like:

```python
W**t t*e h**l am i d***g h**e? A*d w***e is my w****t? P**e s***h!
```

In case you didn't figure out the rules yet: any words longer than 2 characters need to have its "inside" (meaning every character which is not the first or the last) changed into *; as we do not want Pete to scream too much, every uppercase letter which is not at the beginning of the string or coming after a punctuation mark among [".","!","?"] needs to be put to lowercase; spaces and other punctuation marks can be ignored.

Conversely, you need to be sure that the start of each sentence has a capitalized word at the beginning. Sentences are divided by the aforementioned punctuation marks.

Finally, the function will take an additional parameter consisting of an array/list of allowed words which are not to be replaced.

> ALGORITHMS REGULAR EXPRESSIONS DECLARATIVE PROGRAMMING ADVANCED LANGUAGE FEATURES FUNDAMENTALS STRINGS