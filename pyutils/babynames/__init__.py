import fnmatch
import os
import re
import sys

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing pyregex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    res = []
    baby_html = open(filename)
    with baby_html as baby_data:
        text = baby_data.read()
        match = re.search(r'Popularity\sin\s(\d\d\d\d)', text)
        if not match:
            sys.stderr.write("Year not found")
            sys.exit(1)
        # store the year in a list
        res.append(match.group(1))
        # <td>1</td><td>Michael</td><td>Jessica</td>
        name_tuples = re.findall("<td>([0-9]+)</td><td>([a-zA-Z]+)</td><td>([a-zA-Z]+)</td>", text)
        # print(name_tuples)

        # unpack the tuple into a dictionary
        rank_dict = {}
        for rank, boy_name, girl_name in name_tuples:
            if boy_name not in rank_dict:
                rank_dict[boy_name] = rank
            if girl_name not in rank_dict:
                rank_dict[girl_name] = rank
        # print(rank_dict)
        # sort the dictionary alphabetically
        sorted_dict = sorted(rank_dict.keys())
        # print(sorted_dict)

        # match the names to their rank/values
        for name in sorted_dict:
            res.append(name + " " + rank_dict[name])

        # print(res)

    return res


def main():
    """
    This command-line parsing code is provided.
    Make a list of command line arguments, omitting the [0] element
    which is the script itself.

    :return:
    """

    # args = sys.argv[1:]
    #
    # if not args:
    #     print('usage: [--summaryfile] file [file ...]')
    #     sys.exit(1)
    #
    # # Notice the summary flag and remove it from args if it is present.
    # summary = False
    # if args[0] == '--summaryfile':
    #     summary = True
    #     del args[0]

    # +++your code here+++
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    # glob.glob("*.html")
    files = [file for file in os.listdir(path=".") if fnmatch.fnmatch(file, "*.html")]

    for file in files:
        out = extract_names(file)

        text = "\n".join(out)

        outf = open(file[0: len(file) - 5] + '.summary', 'w')
        outf.write(text + '\n')
        outf.close()

        # if true, prints data to a summary file
        # if summary:
        #     outf = open(file + '.summary', 'w')
        #     outf.write(text + '\n')
        #     outf.close()
        # else:
        #     print(text)
    return


if __name__ == '__main__':
    main()
