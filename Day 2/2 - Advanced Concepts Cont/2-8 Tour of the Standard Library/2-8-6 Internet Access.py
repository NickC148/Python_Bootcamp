### 2-8-6 Internet Access ###
# There are a number of modules for accessing the internet and processing internet protocols.
# Two of the simplest are urllib2 for retrieving data from URLs and smtplib for sending mail.

import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:
        print line
# <BR>May. 14, 04:41:01 AM EDT            Eastern Time

# - (Note that this second example needs a mailserver running on localhost.)
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
                """To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
""")
server.quit()
