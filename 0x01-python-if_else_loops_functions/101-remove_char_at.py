#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        # If index is out of bounds, return the original string
        return (str)
    # Construct a new string excluding the character at index n
    return(str[:n] + str[n + 1:])
