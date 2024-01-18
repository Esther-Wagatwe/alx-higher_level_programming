#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        # in python names starting with double underscores are private
        if i[:2] != "__":
            print(i)
