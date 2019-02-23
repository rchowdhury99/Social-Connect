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
        # getting the password from the query
        for i in cursor:
            for item in i:
                if item.encode("ascii") != email:
                    password = (item.encode("ascii")).decode("utf-8")

        return password

    def get_user_info(self, db_name, db_table, email):
        '''Gets the First Name, Last Name'''
        connect = sqlite3.connect(db_name)
        cursor = connect.execute("SELECT Email, FirstName, LastName FROM %s WHERE Email == '%s' " % (db_table, email))
        info = []
        for i in cursor:
            for item in i:
                if (item.encode("ascii")).decode("utf-8") != email:
                    info.append((item.encode("ascii")).decode("utf-8"))

        return info

    def get_social_links(self, db_name, db_table, email):
        '''Gets Social Media Links'''
        connect = sqlite3.connect(db_name)
        cursor = connect.execute("SELECT Email, Facebook, Twitter, Instagram, Snapchat FROM %s WHERE Email == %s" % (db_table, email))
        for i in cursor:
            print(i)
            for item in i:
                if (item.encode("ascii")).decode("utf-8") != email:
                    social_links.append((item.encode("ascii")).decode("utf-8"))

        return social_links


    def add_client(self, db_name, db_table, data):
        connect = sqlite3.connect(db_name)
        # generate command
        # cursor = connect.execute("command")
        return "0" # if saved else return error
