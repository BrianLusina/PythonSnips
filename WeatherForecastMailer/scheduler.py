def get_schedule():
    """
     a tuple, this tuple can then be used to populate the dictionary
    :return: the list of emails
    """
    schedules = {}
    try:
        schedule_file = open('files/schedule.txt', 'r')
        for lines in schedule_file:
            (schedule, time) = lines.split("-")
            schedules[schedule] = time.strip()
    except FileNotFoundError as err:
        print(err, "Oops! File not found, please verify that the file name is correctly spelled.")

    return schedules
