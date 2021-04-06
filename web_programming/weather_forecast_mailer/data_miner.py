import fnmatch
import os


def get_schedule():
    """
    a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    schedules, schedule_list = {}, []
    for file_lists in extension_checker():
        for file in file_lists:
            if file.startswith('schedule'):
                schedule_list.append(file)
    # check if file is a txt file
    for sched_file in schedule_list:
        if sched_file.endswith("txt"):
            try:
                schedule_file = open('files/' + sched_file)
                sched = schedule_file.read()
            except FileNotFoundError as err:
                print(err, "Oops! File not found, please verify that the file name is correctly spelled.")
    return sched


def read_emails():
    """
    Store the emails file in a variable email_file and read each line splitting the line and storing the key,value into
     a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    emails, email_list = {}, []
    for file_lists in extension_checker():
        for file in file_lists:
            if file.startswith('emails'):
                email_list.append(file)
    for email_file in email_list:
        if email_file.endswith("txt"):
            try:
                schedule_file = open('files/' + email_file)
                for lines in schedule_file:
                    (schedule, time) = lines.split(",")
                    emails[schedule] = time.strip()
            except FileNotFoundError as err:
                print(err, "Oops! File not found, please verify that the file name is correctly spelled.")
            schedule_file.close()
    return emails


def extension_checker():
    """
    Retrieves the files from the path specified. This is used to fetch the emails and schedules
    :return: a tuple list with all the files
    """
    txt_files, json_files = [], []
    for file in os.listdir(path='files/'):
        if fnmatch.fnmatch(file, '*.txt'):
            txt_files.append(file)
        if fnmatch.fnmatch(file, '*.json'):
            json_files.append(file)

    return txt_files, json_files
