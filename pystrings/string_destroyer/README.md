Background:

You have a starting string of the lowercase alphabet, space-separated:

"a b c d e f g h i j k l m n o p q r s t u v w x y z"
Then you are given random sets of letters to throw against this string. For example:

{'e', 'B', 'F', 'i'} Whenever there is a match (case sensitive), the letter in the original string is knocked out and
replaced by an underscore. Using the random set above as an example would result in:

"a b c d _ f g h _ j k l m n o p q r s t u v w x y z"
Implementation

Write a function destroyer(input_sets) that takes input as a tuple of one or more of these random character sets and
returns the alphabet formatted as shown, with underscores showing where matches knocked out a letter.

For example:

> > > input_sets = ({'A', 'b'}, {'d', 'C', 'b'})
> > > destroyer(input_sets)
> > > "a _ c _ e f g h i j k l m n o p q r s t u v w x y z"

Extra credit question:

If the average random set thrown at the lowercase alphabet is ten (10) characters long (same rules as above, uppercase
and lowercase letters only), then how many random sets - on average - do you have to throw at the alphabet in order to
be left with only underscores?