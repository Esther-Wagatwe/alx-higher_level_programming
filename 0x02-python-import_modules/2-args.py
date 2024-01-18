#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = len(argv) - 1
    if i < 1:
        print("{} arguments".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))
    for x in range(1, i+1):
        print("{}: {:s}".format(x, argv[x]))
