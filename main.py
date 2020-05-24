#!/usr/bin/env python3


from sys import stdin
import argparse
import re


UNITS = ["k", "m", "g", "t", "p"]


def col(val):
    ival = int(val)
    if ival <= 0:
        raise argparse.ArgumentTypeError(f"{ val } is not a valid column value.")
    return ival


parser = argparse.ArgumentParser(description="Sum sizes.")
parser.add_argument(
    "-b", "--useb", help="print in B instead of iB", action="store_true"
)
parser.add_argument(
    "-u", "--unitless", help="total size is given unitless", action="store_true"
)
parser.add_argument(
    "-f",
    "--figure",
    help="significant figure count after the dot (default 2)",
    type=int,
)
parser.add_argument(
    "-c",
    "--column",
    help="which column to consider as sizes (default 1)",
    type=col,
    default=1,
)
parser.add_argument("-i", "--input", help="read from file instead of stdin")

args = parser.parse_args()


def sumsize(sizes):
    s = 0

    pf = re.compile(r"[K|M|G|T|P]?i?B", re.IGNORECASE)
    ps = re.compile(r"[0-9]+\.?[0-9]*")

    for i in sizes:
        _sizes = ps.findall(i)
        size = float(_sizes[0]) if isinstance(_sizes, list) and len(_sizes) else 0.0

        if size == 0:
            continue

        _factors = pf.findall(i)
        factor = _factors[0].lower() if isinstance(_factors, list) and len(_factors) else "B"

        m = 1
        c = 1024 if "i" in factor else 1000
        for k, w in enumerate(UNITS):
            if w in factor:
                m = c ** (k + 1)
                break

        s += size * m

    return s


def formatsize(size, fig=2, useb=False, unitless=False):
    size = int(size)
    if unitless:
        return str(size)

    c = 1000 if useb else 1024
    for i, j in reversed(list(enumerate(UNITS))):
        m = size / (c ** (i + 1))
        if m > 1:
            f = f"%.{fig}f" % m
            return f"{ f }{ j.upper() }{ '' if useb else 'i' }B"
    return f"{ size }B"


formatinput = lambda x: [re.split("\s", i)[args.column - 1] for i in x]

if args.input is None:
    size = sumsize(formatinput(stdin.readlines()))
else:
    with open(args.input, "r") as f:
        size = sumsize(formatinput(f.readlines()))

if args.figure is not None:
    figure = args.figure
else:
    figure = 2

formattedSize = formatsize(size, fig=figure, useb=args.useb, unitless=args.unitless)

print(formattedSize)
