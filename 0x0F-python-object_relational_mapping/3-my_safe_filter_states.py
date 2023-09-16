#!/usr/bin/python3
"""
     displays all values in the states table of hbtn_0e_0_usa 
     where name matches the argument. 
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
     displays all values in the states table of hbtn_0e_0_usa
     where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    
