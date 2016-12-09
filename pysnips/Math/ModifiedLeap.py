def year_days(year):
    days = 365
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        days += 1
    return "%d has %d days" % (year, days)


print year_days(0), year_days(0) == '0 has 366 days'
print year_days(-64), year_days(-64) == '-64 has 366 days'
print year_days(2016), year_days(2016) == '2016 has 366 days'
print year_days(1974), year_days(1974) == '1974 has 365 days'
print year_days(-10), year_days(-10) == '-10 has 365 days'
print year_days(666), year_days(666) == '666 has 365 days'
print year_days(1857), year_days(1857) == '1857 has 365 days'
print year_days(2000), year_days(2000) == '2000 has 366 days'
print year_days(-300), year_days(-300) == '-300 has 365 days'
print year_days(-1), year_days(-1) == '-1 has 365 days'