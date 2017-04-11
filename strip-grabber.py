import requests
from dateutil import rrule
from datetime import date, timedelta
from time import sleep
import csv

today = date.today()

with open('achewood.txt', 'r+') as datafile, open('404.txt', 'r+') as _404:
    ls = []
    _404s = []
    reader = csv.reader(datafile)
    for row in reader:
        ls.append(row[0])

    reader_404 = csv.reader(_404)
    for row in reader_404:
        ls.append(row[0])

    # set start date
    d = date(2001, 10, 1)
    tt = d.timetuple()

    # difference from start date to today
    today = date.today()
    difference = today - d

    # set number of days to spin through
    daysLater = d + timedelta(difference.days)

    # the loop
    for day in rrule.rrule(rrule.DAILY, dtstart=d, until=daysLater):

        month = '{0:02d}'.format(day.month)
        date = '{0:02d}'.format(day.day)
        year = str(day.year)

        datestring = month + date + year

        if datestring not in ls and datestring not in _404s:

            comic = 'http://achewood.com/comic.php?date={}'.format(datestring)
            r = requests.get(comic)

            if r.status_code == 404:
                _404s.append(datestring)
                _404.write(datestring + '\n')
            else:
                ls.append(datestring)
                print(comic)
                datafile.write(datestring + '\n')

            sleep(2)
