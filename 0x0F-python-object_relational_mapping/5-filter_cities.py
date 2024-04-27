#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    connector = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    cur = connector.cursor()
    cur.execute("SELECT cities.name FROM cities \
                JOIN states ON cities.state_id = states.id \
                WHERE states.name = %s \
                ORDER BY cities.id", (argv[4], ))
    rows = cur.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))
    cur.close()
    connector.close()
