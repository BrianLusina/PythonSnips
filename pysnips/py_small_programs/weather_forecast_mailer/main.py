from WeatherForecastMailer import data_miner, smtp, weather


def main():
    emails = data_miner.read_emails()
    schedule = data_miner.get_schedule()
    forecast = weather.get_current_weather_forecast("Nairobi")

    smtp.send_emails(emails=emails, schedule=schedule, forecast=forecast)


main()
