You left your computer unlocked and your friend decided to troll you by copying a lot of your files to random spots all
over your file system. Even worse, she saved the duplicate files with random, embarrassing names ("
this_is_like_a_digital_wedgie.txt" was clever, I'll give her that).

Write a function that returns a list of all the duplicate files. We'll check them by hand before actually deleting them,
since programmatically deleting files is really scary. To help us confirm that two files are actually duplicates, return
a list of tuples ↴ A tuple is a list of elements:

(17, 3, "My name is Parker")
Python
(Tuples are usually notated with parentheses to differentiate them from lists.)

Like lists, tuples are ordered and you can access elements by their index:

cake_tuple = ('angel', 'bundt')

cake_tuple[0]

# returns: 'angel'

Python But tuples are immutable! They can't be edited after they're created.

cake_tuple = ('angel', 'bundt')
cake_tuple[1] = 'carrot'

# raises: TypeError: 'tuple' object does not support item assignment

Python Tuples can have any number of elements (the 'tu' in tuple doesn't mean 'two', it's just a generic name taken from
words like 'septuple' and 'octuple').

(90, 4, 54)
(True, False, True, True, False)
Python where:

the first item is the duplicate file the second item is the original file For example:

[('/tmp/parker_is_dumb.mpg', '/home/parker/secret_puppy_dance.mpg'),
('/home/trololol.mov', '/etc/apache2/httpd.conf')]
You can assume each file was only duplicated once.

Breakdown No idea where to start? Try writing something that just walks through a file system and prints all the file
names. If you're not sure how to do that, look it up! Or just make it up. Remember, even if you can’t implement working
code, your interviewer will still want to see you think through the problem.

One brute force ↴ A brute force algorithm simply enumerates all possible answers to the question and checks them for
correctness.

It's seldom the most efficient approach, but it can be helpful to consider the time cost of the brute force approach
when building an optimized solution. If your solution isn't faster than the brute force approach, it may not be optimal.
solution is to loop over all files in the file system, and for each file look at every other file to see if it's a
duplicate. This means n^2n ​2 ​​ file comparisons, where nn is the number of files. That seems like a lot.

Let's try to save some time. Can we do this in one walk through our file system?

Instead of holding onto one file and looking for files that are the same, we can just keep track of all the files we've
seen so far. What data structure could help us with that?

We'll use a dictionary ↴ A hash table (also called a hash, hash map, map, unordered map or dictionary) is a data
structure that pairs keys to values.

lightbulb_to_hours_of_light = {
'incandescent': 1200,
'compact fluorescent': 10000,
'LED': 50000 }

Hash tables:

take on average O(1)O(1) time for insertions and lookups are unordered (the keys are not guaranteed to stay in the same
order)
can use many types of objects as keys (commonly strings)
Hash tables can be thought of as arrays, if you think of array indices as keys!

In fact, hash tables are built on arrays. So if you ever want to use a hash table but know your keys will be sequential
integers (like 1..1001..100), you can probably save time and space by just using an array instead.

Note: hash tables have an average case insertion and lookup cost of O(1)O(1). In industry, we often confuse the
average-case cost with worst case cost, but they're not really the same. Because of hash collisions and rebalancing, a
hash table insertion or lookup can cost as much as O(n)O(n) time in the worst case. But usually in industry we assume
hashing and resizing algorithms are clever enough that collisions are rare and cheap. . When we see a new file, we first
check to see if it's in our dictionary. If it's not, we add it. If it is, we have a duplicate!

Once we have two duplicate files, how do we know which one is the original? It's hard to be sure, but try to come up
with a reasonable heuristic that will probably work most of the time.

Most file systems store the time a file was last edited as metadata on each file. The more recently edited file will
probably be the duplicate!

One exception here: lots of processes like to regularly save their state to a file on disc, so that if your computer
suddenly crashes the processes can pick up more or less where they left off (this is how Word is able to say "looks like
you had unsaved changes last time, want to restore them?"). If your friend duplicated some of those files, the
most-recently-edited one may not be the duplicate. But at the risk of breaking our system (we'll make a backup first,
obvi.) we'll run with this "most-recently-edited copy of a file is probably the copy our friend made" heuristic.

So our function will walk through the file system, store files in a dictionary, and identify the more recently edited
file as the copied one when it finds a duplicate. Can you implement this in code?

Here's a start. We'll initialize:

a dictionary to hold the files we've already seen a stack (we'll implement ours with a list) to hold directories and
files as we go through them a list to hold our output tuples def find_duplicate_files_iterative(starting_directory):
files_seen_already = {} stack = [starting_directory]

    # we'll track tuples of (duplicate_file, original_file)
    duplicates = []

    while len(stack):

        current_path = stack.pop()

(We're going to make our function iterative instead of recursive to avoid stack overflow ↴ The call stack is what a
program uses to keep track of what function it's currently running and what to do with that function's return value.

Whenever you call a function, a new frame gets pushed onto the call stack, which is popped off when the function
returns. As functions call other functions, the stack gets taller. In recursive functions, the stack can get as tall as
the number of times the function calls itself. This can cause a problem: the stack has a limited amount of space, and if
it gets too big you can get a stack overflow error. .)

Here's one solution:

``` python
  import os

def find_duplicate_files_iterative(starting_directory):
    files_seen_already = {}
    stack = [starting_directory]

    # we'll track tuples of (duplicate_file, original_file)
    duplicates = []

    while len(stack) > 0:

        current_path = stack.pop()

        # if it's a directory,
        # put the contents in our stack
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                full_path = os.path.join(current_path, path)
                stack.append(full_path)

        # if it's a file
        else:

            # get its contents
            with open(current_path) as file:
                file_contents = file.read()

            # get its last edited time
            current_last_edited_time = os.path.getmtime(current_path)

            # if we've seen it before
            if file_contents in files_seen_already:

                existing_last_edited_time, existing_path = files_seen_already[file_contents]

                if current_last_edited_time > existing_last_edited_time:
                    # current file is the dupe!
                    duplicates.append((current_path, existing_path))

                else:
                    # old file is the dupe!
                    # so delete it
                    duplicates.append((existing_path, current_path))

                    # but also update files_seen_already to have the new file's info
                    files_seen_already[file_contents] = \
                        (current_last_edited_time, current_path)

            # if it's a new file, throw it in files_seen_already
            # and record the path and the last edited time,
            # so we can delete it later if it's a dupe
            else:
                files_seen_already[file_contents] = \
                    (current_last_edited_time, current_path)

    return duplicates
```

Okay, this'll work! What are our time and space costs?

We're putting the full contents of every file in our dictionary! This costs O(b)O(b) time and space, where bb is the
total amount of space taken up by all the files on the file system.

That space cost is pretty unwieldy—we need to store a duplicate copy of our entire filsystem (like, several gigabytes of
cat videos alone) in working memory!

Can we trim that space cost down? What if we're okay with losing a bit of accuracy (as in, we do a more "fuzzy" match to
see if two files are the same)?

What if instead of making our dictionary keys the entire file contents, we hashed ↴ A hash function takes data (like a
string, or a file’s contents) and outputs a hash, a fixed-size string or number.

For example, here’s the MD5 hash (MD5 is a common hash function) for a file simply containing “cake”:

DF7CE038E2FA96EDF39206F898DF134D And here’s the hash for the same file after it was edited to be “cakes”:

0E9091167610558FDAE6F69BD6716771 Notice the hash is completely different, even though the files were similar. Here's the
hash for a long film I have on my hard drive:

664f67364296d08f31aec6fea4e9b83f The hash is the same length as my other hashes, but this time it represents a much
bigger file—461Mb.

We can think of a hash as a "fingerprint." We can trust that a given file will always have the same hash, but we can't
go from the hash back to the original file. Sometimes we have to worry about multiple files having the same hash value,
which is called a hash collision.

Some uses for hashing:

Dictionaries. Suppose we want a list-like data structure with constant-time lookups, but we want to look up values based
on arbitrary "keys," not just sequential "indices." We could allocate a list, and use a hash function to translate keys
into list indices. That's the basic idea behind a dictionary!
Preventing man-in-the-middle attacks. Ever notice those things that say "hash" or "md5" or "sha1" on download sites? The
site is telling you, "We hashed this file on our end and got this result. When you finish the download, try hashing the
file and confirming you get the same result. If not, your internet service provider or someone else might have injected
malware or tracking software into your download!"
those contents first? So we'd store a constant-size "fingerprint" of the file in our dictionary, instead of the whole
file itself. This would give us O(1)O(1) space per file (O(n)O(n) space overall, where nn is the number of files)!

That's a huge improvement. But we can take this a step further! While we're making the file matching "fuzzy," can we use
a similar idea to save some time? Notice that our time cost is still order of the total size of our files on disc, while
our space cost is order of the number of files.

For each file, we have to look at every bit that the file occupies in order to hash it and take a "fingerprint." That's
why our time cost is high. Can we fingerprint a file in constant time instead?

What if instead of hashing the whole contents of each file, we hashed three fixed-size "samples" from each file made of
the first xx bytes, the middle xx bytes, and the last xx bytes? This would let us fingerprint a file in constant time!

How big should we make our samples?

When your disc does a read, it grabs contents in constant-size chunks, called "blocks."

How big are the blocks? It depends on the file system. My super-hip Macintosh uses a file system called HFS+, which has
a default block size of 4Kb (4,000 bytes) per block.

So we could use just 100 bytes each from the beginning middle and end of our files, but each time we grabbed those
bytes, our disc would actually be grabbing 4000 bytes, not just 100 bytes. We'd just be throwing the rest away. We might
as well use all of them, since having a bigger picture of the file helps us ensure that the fingerprints are unique. So
our samples should be the the size of our file system's block size.

We walk through our whole file system iteratively. As we go, we take a "fingerprint" of each file in constant time by
hashing the first few, middle few, and last few bytes. We store each file's fingerprint in a dictionary as we go.

If a given file's fingerprint is already in our dictionary, we assume we have a duplicate. In that case, we assume the
file edited most recently is the one created by our friend.

## Assumptions

We've made a few assumptions here:

Two different files won't have the same fingerprints. It's not impossible that two files with different contents will
have the same beginning, middle, and end bytes so they'll have the same fingerprints. Or they may even have different
sample bytes but still hash to the same value (this is called a "hash collision"). To mitigate this, we could do a
last-minute check whenever we find two "matching" files where we actually scan the full file contents to see if they're
the same.

The most recently edited file is the duplicate. This seems reasonable, but it might be wrong—for example, there might be
files which have been edited by daemons (programs that run in the background) after our friend finished duplicating
them.

Two files with the same contents are the same file. This seems trivially true, but it could cause some problems. For
example, we might have empty files in multiple places in our file system that aren't duplicates of each-other.

Given these potential issues, we definitely want a human to confirm before we delete any files. Still, it's much better
than combing through our whole file system by hand!

## Ideas for improvement

Some ideas for further improvements:

1. If a file wasn't last edited around the time your friend got a hold of your computer, you know it probably wasn't
   created by your friend. Similarly, if a file wasn't accessed (sometimes your filesystem stores the last accessed time
   for a file as well) around that time, you know it wasn't copied by your friend. You can use these facts to skip some
   files.

2. Make the file size the fingerprint—it should be available cheaply as metadata on the file (so you don't need to walk
   through the whole file to see how long it is). You'll get lots of false positives, but that's fine if you treat this
   as a "pre-processing" step. Maybe you then take hash-based fingerprints only on the files which which have matching
   sizes. Then you fully compare file contents if they have the same hash.

3. Some file systems also keep track of when a file was created. If your filesystem supports this, you could use this as
   a potentially-stronger heuristic for telling which of two copies of a file is the dupe.

4. When you do compare full file contents to ensure two files are the same, no need to read the entire files into
   memory. Open both files and read them one block at a time. You can short-circuit as soon as you find two blocks that
   don't match, and you only ever need to store a couple blocks in memory.

Complexity Each "fingerprint" takes O(1)O(1) time and space, so our total time and space costs are O(n)O(n) where nn is
the number of files on the file system.

If we add the last-minute check to see if two files with the same fingerprints are actually the same files (which we
probably should), then in the worst case all the files are the same and we have to read their full contents to confirm
this, giving us a runtime that's order of the total size of our files on disc.

Bonus If we wanted to get this code ready for a production system, we might want to make it a bit more modular. Try
separating the file traversal code from the duplicate detection code. Try implementing the file traversal with a
generator!

What about concurrency? Can we go faster by splitting this procedure into multiple threads? Also, what if a background
process edits a file while our script is running? Will this cause problems?

What about link files (files that point to other files or folders)? One gotcha here is that a link file can point back
up the file tree. How do we keep our file traversal from going in circles?

What We Learned The main insight was to save time and space by "fingerprinting" each file.

This question is a good example of a "messy" interview problem. Instead of one optimal solution, there's a big knot of
optimizations and trade-offs. For example, our hashing-based method wins us a faster runtime but it can give us false
positives.

For messy problems like this, focus on clearly explaining to your interviewer what the trade-offs are for each decision
you make. The actual choices you make probably don't matter that much, as long as you show a strong ability to
understand and compare your options.