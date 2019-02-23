import os
import sqlite3
from datetime import datetime

class Database(object):
    def login_info(self, db_name, db_table, email):
        '''Checks for the password for the requested email'''
        connect = sqlite3.connect(db_name)
        # getting the password back
        cursor = connect.execute("SELECT Email, Password FROM %s WHERE EMAIL == '%s'" % (db_table, email))
        # password for the email if exists
        password = None
        for i in cursor:
            for item in i:
                if item.encode("ascii") != email:
                    password = item.encode("ascii")

        print("DB-Password: %s" % (password))
        return password


    def get(self, db_name, db_table):
        '''
        Returns table rows given a table
        Args: db_name, db_table
        Returns: columns(list), rows(list)
        '''
        connect = sqlite3.connect(db_name)
        cursor = connect.cursor()
        # getting rows
        x = cursor.execute("SELECT * FROM %s" % (db_table)).fetchall()
        # getting columns
        columns = list(map(lambda x: x[0], cursor.description))
        # seperating rows
        rows = []
        for i in x:
            rows.append(list(i))

        # returning rows and columns
        return [columns, rows]
