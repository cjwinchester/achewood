import urllib
import os
from dateutil import rrule
from datetime import *
from time import *

# set start date
d = date(2001, 10, 01)
tt = d.timetuple()

# difference from start date to today
today = date.today()
difference = today - d

# set number of days to spin through
daysLater = d + timedelta(difference.days)

# the loop
for thing in rrule.rrule(rrule.DAILY, dtstart=d, until=daysLater):
    year = str(thing)[:4]
    month = str(thing)[5:7]
    day = str(thing)[8:10]
    
    # create empty gif
    filename = year + month + day + '.gif'
    f = open(filename,'wb')
    print 'Grabbing Achewood for ' + month + '/' + day + '/' + year
    
    # write content
    f.write(urllib.urlopen('http://achewood.com/comic.php?date=' + month + day + year).read())
    f.close()
    sleep(3)

# delete empty files for days without a strip
os.chdir("/Users/Winchester/Desktop/achewood")
for file in os.listdir("."):
    if file.st_size == 0:
        os.remove(file)
        print 'Cleaning up ...'
