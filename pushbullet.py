#!/usr/bin/env python
from urllib import urlopen, urlencode
import sys
import os
key = os.environ['PUSHBULLET_APIKEY']
device = os.environ['PUSHBULLET_IPHONE']

def note(title, body):
  params = urlencode({
    "device_iden": device,
    "type": "note",
    "title": title,
    "body": body
    })
  urlopen("https://%s:@api.pushbullet.com/api/pushes" % key, params)

def link(title, url):
  params = urlencode({
    "device_iden": device,
    "type": "link",
    "title": title,
    "url": url 
    })
  urlopen("https://%s:@api.pushbullet.com/api/pushes" % key, params)

def main():
  ntype, title, url_body = sys.argv[1:]
  if ntype == "note":
    note(title, url_body)
  if ntype == "link":
    link(title, url_body)

if __name__ == "__main__":
  main()
