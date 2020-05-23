#!/usr/bin/env python3


from sys import stdin
import argparse
import re


UNITS = [ "k", "m", "g", "t", "p" ]

parser = argparse.ArgumentParser(description="Sum sizes.")
parser.add_argument("-b", "--useb", help="use B instead of iB", action="store_true")
parser.add_argument("-f", "--figure", help="significant figure count after the dot", type=int)

args = parser.parse_args()


def sumsize(sizes):
    s = 0

    pf = re.compile(r"[K|M|G|T|P]?i?B", re.IGNORECASE)
    ps = re.compile(r"[0-9]+\.?[0-9]*")

    for i in sizes:
        _factors = pf.findall(i)
        factor = _factors[0].lower() if isinstance(_factors, list) else "B"

        _sizes = ps.findall(i)
        size = float(_sizes[0]) if isinstance(_sizes, list) else 0.0

        m = 1
        c = 1024 if "i" in factor else 1000
        for k, w in enumerate(UNITS):
            if w in factor:
                m = c ** (k + 1)
        
        s += size * m

    return s


def formatsize(size, F=2, B=False):
    c = 1000 if B else 1024
    for i, j in reversed(list(enumerate(UNITS))):
        m = size / (c ** (i + 1))
        if m > 1:
            f = f"%.{F}f" % m
            return f"{ f }{ j.upper() }{ '' if B else 'i' }B"
    return f"{ size }B"


stdinLines = stdin.readlines()
size = sumsize(stdinLines)

useB = args.useb

figure = 2
if args.figure is not None:
    figure = args.figure 

f = formatsize(size, F=figure, B=useB)

print(f)
