#!/bin/env python
import sys

def decode(tokens):
    x = 0
    print(tokens)
    print("")
    for c in tokens:
        sys.stdout.write(chr(ord(c)-x))
        x = x+1
    print("")

decode("857:g67?5ABBo:BtDA?tIvLDKL{MQPSRQWW.")
