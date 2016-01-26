#!/usr/bin/python

import sys

if len(sys.argv) !=3:
    print 'Usage: tail.py <file> <nlines>'
    sys.exit(1)

fname, nlines = sys.argv[1:]
num_lines = int(nlines)

with open(fname) as f:
    content = f.read().splitlines()

count = len(content)
for i in range(count-num_lines,count):
  print content[i]

