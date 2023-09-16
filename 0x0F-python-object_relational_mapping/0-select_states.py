#!/usr/bin/python3
"""
    script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
        Results must be sorted in ascending order by states.id
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                        passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
