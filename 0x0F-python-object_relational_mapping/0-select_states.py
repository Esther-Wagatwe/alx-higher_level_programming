#!/usr/bin/python3
"""Script that lists all states from a database."""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    cur = connector.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connector.close()
