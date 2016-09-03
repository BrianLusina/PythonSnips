from pprint import pprint
from WeatherForecastMailer import emailer


def main():
    emails = emailer.read_emails()
    pprint(emails)

main()
