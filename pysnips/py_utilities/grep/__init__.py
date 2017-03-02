def grep(pattern, files, flags=""):
    """
    Similar to the UNIX grep command which searches through files and strings for a pattern and returns
    the result if found.
    :param pattern: the pattern to search for
    :param files: files to search through, at least one file, given as a list
    :param flags: the flags to use, default is "", ie. no flags
    :return: A string with the match from either the files or the file names where the match exists
    :rtype: str
    """
    matched_lines = []

    for file_name in files:
        with open(file_name) as file:
            for line_number, line in enumerate(file.readlines(), start=1):
                if matches(line=line, pattern=pattern, flags=flags):
                    matched_lines.append((file_name, line_number, line))

    if "-l" in flags:
        return format_files(matched_lines)

    return format_lines(matched_lines, files=files, flags=flags)


def matches(line, pattern, flags):
    """
    Checks if the pattern is in the line currently being searched. Uses the flags to modify the patter and/or the
    line being searched through.
    `-i` Match line using a case-insensitive comparison.
    `-v` Invert the program -- collect all lines that fail to match the pattern.
    `-x` Only match entire lines, instead of lines that contain a match.
    :param line: the line to search through in the file or the string provided
    :param pattern: the pattern to use for the search
    :param flags: the flags to narrow down the search
    :return: Boolean value, returns True if the pattern is in the line
    :rtype: bool
    """
    # case insensitive, change the variables cases
    if "-i" in flags:
        pattern = pattern.lower()
        line = line.lower()

    # invert matching, will check if the patter is not in line, return True/False whether it is.
    if "-v" in flags:
        return pattern not in line

    # match an entire line
    if "-x" in flags:
        if len(line.rstrip()) != len(pattern):
            return False

    return pattern in line


def format_files(matched_lines):
    """
    This is triggered if the pattern being sought is in a line that is contained in a file
    `-l` Print only the names of files that contain at least one matching line.
    The matched lines will contain a tuple with the
    1st param being the file name
    2nd param being the line number and
    3rd param being the line matched
    :param matched_lines: the lines that are matched as a list
    :return: a string with the file names
    :rtype: str
    """
    output = ""

    # since we are only interested in the file names, we `dash` out the line number and the lines matched
    for file_name, _, _ in matched_lines:
        if file_name not in output:
            output += file_name + "\n"

    return output


def format_lines(matched_lines, files, flags):
    """
    This formats the result of the find if the pattern is in a certain line in a file.
    If -n is in the flags the line number will be included in the search result
        `-n` Print the line numbers of each matching line.
    :param matched_lines: a list with 1 tuple containing file_name, line_number and line
    :param files: files to search for the matching pattern, will be a list
    :param flags: The flags to use for the search
    :return: a formatted search result
    :rtype: str
    """
    search_result = []

    for file_name, line_number, line in matched_lines:
        line_result = ""

        if len(files) > 1:
            line_result += file_name + ":"

        if "-n" in flags:
            line_result += str(line_number) + ":"

        line_result += line

        search_result.append(line_result)

    return "".join(search_result)
