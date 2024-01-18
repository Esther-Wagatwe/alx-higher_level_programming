#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__": #names starting with double underscores are considered private in python
            print(i)
