from WeatherForecastMailer import data_miner, smtp, weather


def main():
    emails = data_miner.read_emails()
    schedule = data_miner.get_schedule()
    forecast = weather.current_weather

    smtp.send_emails(emails=emails, schedule=schedule, forecast=forecast)

main()
