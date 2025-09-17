#!/usr/bin/env python3

from calendar import day_abbr
from ctypes import sizeof
import re


def file_listing(filename="src/listing.txt"):
    with open(filename, "r") as f:
        vals = []
        for line in f:
            parse = re.findall(r"\s*(\S+)", line)
            rights, references, uname, owner, size, month, day, time, fname = parse
            sTimes = time.split(":")
            vals.append((int(size), month, int(day), int(sTimes[0]), int(sTimes[1]), fname))
        return vals
        #(size, month, day, hour, minute, filename)

def main():
    file_listing()

    #Begin tests
    result = file_listing()
    print(len(result))
    #Output should be: 47

    for i in result:
       print(len(i))
    #Output should all be 6s as the length of each item is 6

#rights references name owner size date name

    for t in result:
        print(f"Items in result should be tuples and they are {type(t)}")
        print(f"First item in tuple should be an str, is {type(t[0])}")
        print(f"Second item in tuple should be an int, is {type(t[1])}")
        print(f"Third item in tuple should be an int, is {type(t[2])}")
        print(f"Fourth item in tuple should be an int, is {type(t[3])}")
        print(f"Fifth item in tuple should be an int, is {type(t[4])}")
        print(f"Sixth item in tuple should be an str, is {type(t[5])}")



if __name__ == "__main__":
    main()
