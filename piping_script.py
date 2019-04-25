#!/usr/bin/env python

import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description='Push tests to Polarion.')
    parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', type=argparse.FileType('w'), default=sys.stdout)
    
    args = parser.parse_args()
    for line in args.infile:
        args.outfile.write(line)

#identify if there is a relevant pattern
#pass pattern to Polarion to upload and to receive token
#modify the line that will be written to the outfile
#write line to outfile

def check_for_pattern(line):
    pass


if __name__ == "__main__":
    main()
