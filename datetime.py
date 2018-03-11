import datetime
def daysBetweenDates():
    year = datetime.date.today().year
    month = datetime.date.today().month
    day = datetime.date.today().day
    date1 = datetime.date(int(raw_input("Enter your year")),int(raw_input("Enter your month")),int(raw_input("Enter your day")))
    date2 = datetime.date(year,month,day)
    year_to_days = date2 - date1
    print "Your age is " + str(year_to_days)
daysBetweenDates()