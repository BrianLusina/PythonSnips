"""
You can open files in write-only mode ("w"), read-only mode ("r"), read and write mode ("r+"), and append mode ("a", which adds any new data you write to the file to the end of the file).
We can write to a Python file like so:
"""
my_file.write("Data to be written")
"""
The write() function takes a string argument, so we'll need to do a few things here:
You must close the file. You do this simply by calling my_file.close() (we did this for you in the last exercise). If you don't close your file, Python won't write to it properly.

During the I/O process, data is buffered: this means that it is held in a temporary location before being written to the file.
Python doesn't flush the buffer—that is, write data to the file—until it's sure you're done writing. One way to do this is to close the file. If you write to a file without closing, the data won't make it to the target file.

You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren't important, but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as.

The syntax looks like this:

with open("file", "mode") as variable:
    # Read or write to the file

Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?
"""

f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True
"""
Python file objects have a closed attribute which is True when the file is closed and False otherwise.

By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.
"""