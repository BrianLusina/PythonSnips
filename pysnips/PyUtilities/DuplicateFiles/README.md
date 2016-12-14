You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all over your file system.
Even worse, she saved the duplicate files with random, embarrassing names ("this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them, since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return a list of tuples ↴
A tuple is a list of elements:

  (17, 3, "My name is Parker")
Python
(Tuples are usually notated with parentheses to differentiate them from lists.)

Like lists, tuples are ordered and you can access elements by their index:

  cake_tuple = ('angel', 'bundt')

cake_tuple[0]
# returns: 'angel'
Python
But tuples are immutable! They can't be edited after they're created.

   cake_tuple = ('angel', 'bundt')
cake_tuple[1] = 'carrot'
# raises: TypeError: 'tuple' object does not support item assignment
Python
Tuples can have any number of elements (the 'tu' in tuple doesn't mean 'two', it's just a generic name taken from words like 'septuple' and 'octuple').

   (90, 4, 54)
(True, False, True, True, False)
Python
where:

the first item is the duplicate file
the second item is the original file
For example:

  [('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
 ('/home/trololol.mov', '/etc/apache2/httpd.conf')]
You can assume each file was only duplicated once.

Breakdown
No idea where to start? Try writing something that just walks through a file system and prints all the file names. If you're not sure how to do that, look it up! Or just make it up. Remember, even if you can’t implement working code, your interviewer will still want to see you think through the problem.

One brute force ↴
A brute force algorithm simply enumerates all possible answers to the question and checks them for correctness.

It's seldom the most efficient approach, but it can be helpful to consider the time cost of the brute force approach when building an optimized solution. If your solution isn't faster than the brute force approach, it may not be optimal.
solution is to loop over all files in the file system, and for each file look at every other file to see if it's a duplicate. This means n^2n
​2
​​  file comparisons, where nn is the number of files. That seems like a lot.

Let's try to save some time. Can we do this in one walk through our file system?