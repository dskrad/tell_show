#!/usr/bin/env python
"""Pushbullet.py
Usage:
  pushbullet.py note <title> [<body>] [<email>]
  pushbullet.py link <title> <url> [<email>]
  pushbullet.py list <title> <list_items> ...
  pushbullet.py --version
  pushbullet.py (-h | --help)

Options:
  -h --help   Show this screen
  --version   Show version
"""
import requests as R
import sys
from secrets import PUSHBULLET_APIKEY
key = PUSHBULLET_APIKEY
#device = os.environ['PUSHBULLET_IPHONE']
URL = "https://api.pushbullet.com/v2/pushes"

def note(title, body="", email=""):
  params = {
    #"device_iden": device,
    "type": "note",
    "title": title,
    "body": body,
    "email": email}
  R.post(URL, params, auth=(key,""))

def link(title, url, email=""):
  params = {
    #"device_iden": device,
    "type": "link",
    "title": title,
    "url": url,
    "email": email}
  R.post(URL, params, auth=(key,""))

def list_(title, items=[], email=""):
  params = {
    #"device_iden": device,
    "type": "list",
    "title": title,
    "items": items,
    "email": email}
  r = R.post(URL, json=params, auth=(key, ""))

def main():
  if args["note"]:
    note(args['<title>'], args['<body>'],
         args['<email>'])
  elif args["link"]:
    link(args['<title>'], args['<url>'],
         args['<email>'])
  elif args["list"]:
    list_(args['<title>'], args['<list_items>'])

if __name__ == "__main__":
  from docopt import docopt
  args = docopt(__doc__, version="0.8")
  main()
