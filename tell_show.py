#!/usr/bin/env python
import datetime as dt
from time import sleep
import re
import pushbullet
from urllib import urlopen
from bs4 import BeautifulSoup as bs

base = "http://www.thefutoncritic.com/listings/"
now = dt.date.today()

def check_shows(date,*shows):
  url = base+date.strftime("%Y/%m/%d/")
  soup = bs(urlopen(url))
  msg = [date.strftime("%a %m/%d")]
  for show in shows:
    pat = re.compile(r"(?:\n)(%s)" % show)
    regmatch = re.search(pat, soup.text)
    if regmatch != None:
      msg.append(regmatch.group(1).upper())
  if len(msg) > 1:  
    return " * ".join(msg) 

def week_of_shows(*shows):
  for i in range(7):
    day = now + dt.timedelta(i)
    yield check_shows(day,*shows)

shws = [x.strip() for x in open(".tell_show","r").readlines()]
results = "\n".join([ msg for msg in week_of_shows(*shws) if msg ])
pushbullet.note("New TV this week!", results)
print "Results"
print results
