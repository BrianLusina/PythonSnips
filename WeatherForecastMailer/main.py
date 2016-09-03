from pprint import pprint
from WeatherForecastMailer import data_miner


def main():
    emails = data_miner.read_emails()
    pprint(emails)

main()
