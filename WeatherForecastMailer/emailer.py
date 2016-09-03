from pprint import pprint


def read_emails():
    """
    Store the emails file in a variable email_file and read each line splitting the line and storing the key,value into
     a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    emails = {}
    try:
        email_file = open('emails.txt', 'r+')
        for lines in email_file:
            (email, name) = lines.split(",")
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err, "Oops! File not found, please verify that the file name is correctly spelled.")

    return emails


def get_schedule():
    """
     a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    schedules = {}
    try:
        schedule_file = open('schedule.txt', 'r')
        for lines in schedule_file:
            (schedule, time) = lines.split("-")
            schedules[schedule] = time.strip()
    except FileNotFoundError as err:
        print(err, "Oops! File not found, please verify that the file name is correctly spelled.")

    return schedules


def main():
    emails = read_emails()
    pprint(emails)

    schedule = get_schedule()
    pprint(schedule)

main()
