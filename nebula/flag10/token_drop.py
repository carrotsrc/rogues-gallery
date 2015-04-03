#!/bin/env python

import os
import sys
import socket
from thread import *

def clientthread(conn):
    reply = ""
    while True:
        data = conn.recv(1024)
        reply += data
        if not data:
            break
    if reply != ".oO Oo.\n":
        print reply

    conn.close()
print "Starting..."
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 18211))
    s.listen(1)
except socket.error as msg:
    colorPrintLine("FAIL", "31")
    print "Exception occured [" + str(msg[0]) +"]\n"+msg[1]
    sys.exit()

print "OK\nWaiting...\n"
while 1:
    conn, addr = s.accept()
    start_new_thread(clientthread ,(conn,))
conn.close()
