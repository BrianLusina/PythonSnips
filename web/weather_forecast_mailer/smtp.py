import smtplib

from WeatherForecastMailer import constants


def send_emails(emails, schedule, forecast):
    """
    server is an SMTP object that takes in a host and port number, either TLS, or SSL,
    TLS is used in this case, the host is smtp.gmail.com
    we then start the server and login. The login requires an email address  and the password to your email address
    For loop is used to send data to each individual email attaching a message. We then quit the server
    :param emails: emails to send to
    :param schedule: schedule to attach
    :param forecast: forecasts to send
    :return: Nothing is returned as this is simply used to temporarily connect to server, perform operations and close server.
    """
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)

    # start TCL server
    server.starttls()

    # login
    from_email = constants.email_sender
    password = constants.password

    # login to server
    server.login(user=from_email, password=password)

    # send email to entire email dictionary
    for to_email, name in emails.items():
        message = "Subject: " + "Today's forecast\n"
        message += "Hi, " + name + "!\n\n"
        message += forecast + "\n\n"
        message += schedule + "\n\n"

        server.sendmail(to_addrs=to_email, from_addr=from_email, msg=message)

    # close the server
    server.quit()
