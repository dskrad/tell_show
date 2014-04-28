#!/usr/bin/env python
import requests as r
import sys
import os
key = os.environ['PUSHBULLET_APIKEY']
device = os.environ['PUSHBULLET_IPHONE']
url = "https://api.pushbullet.com/api/pushes"

def note(title, body):
  params = {
    "device_iden": device,
    "type": "note",
    "title": title,
    "body": body
  }
  r.post(url, auth=(key,""), data=params)

def link(title, url):
  params = {
    "device_iden": device,
    "type": "link",
    "title": title,
    "url": url 
  }
  r.post(url, auth=(key,""), data=params)

def main():
  if len(sys.argv) != 4:
    print "Incorrect number of args. Usage:"
    print "\tpushbullet note note_title note_body"
    print "\tpushbullet link title url"
  else:
    ntype, title, url_body = sys.argv[1:]
    if ntype == "note":
      note(title, url_body)
    if ntype == "link":
      link(title, url_body)

if __name__ == "__main__":
  main()
