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
    factors = [j[0].lower() if isinstance(j, list) else None for j in [re.findall(r"[K|M|G|T|P]?i?B", i, re.IGNORECASE) for i in sizes]]
    sizes = [float(j[0]) if isinstance(j, list) else 0.0 for j in [re.findall(r"[0-9]+\.?[0-9]*", i) for i in sizes]]
    realSizes = []

    for i, j in enumerate(sizes):
        factor = factors[i]
        if factor is None:
            continue
        m = 1

        c = 1024 if "i" in factor else 1000
        for k, w in enumerate(UNITS):
            if w in factor:
                m = c ** (k + 1)

        realSizes.append(j * m)

    return sum(realSizes)


def formatsize(size, n=2, I=True):
    c = 1024 if I else 1000
    for i, j in reversed(list(enumerate(UNITS))):
        m = size / (c ** (i + 1))
        if m > 1:
            f = f"%.{n}f" % m
            return f"{ f }{ j.upper() }{ 'i' if I else '' }B"
    return f"{ size }B"


stdinLines = stdin.readlines()
size = sumsize(stdinLines)

useB = not args.useb

figure = 2
if args.figure is not None:
    figure = args.figure 

f = formatsize(size, n=figure, I=useB)

print(f)
