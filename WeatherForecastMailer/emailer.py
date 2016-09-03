import os
import fnmatch


def read_emails():
    """
    Store the emails file in a variable email_file and read each line splitting the line and storing the key,value into
     a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    emails = {}
    try:
        email_file = open('files/emails.txt', 'r+')
        for lines in email_file:
            (email, name) = lines.split(",")
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err, "Oops! File not found, please verify that the file name is correctly spelled.")

    return emails


def extension_checker(path):
    """
    Retrieves the files from the path specified. This is used to fetch the emails and schedules
    :param path of the files to retrieve date from
    :return: a tuple list with all the files
    """
    txt_files, json_files = [], []
    for file in os.listdir(path=path):
        if fnmatch.fnmatch(file, '*.txt'):
            txt_files.append(file)
        if fnmatch.fnmatch(file, '*.json'):
            json_files.append(file)

    return txt_files, json_files

print(extension_checker('files/'))
