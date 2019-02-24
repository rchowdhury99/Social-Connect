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

    def get_user_name(self, db_name, db_table, email):
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

    def add_client(self, db_name, db_table, columns, values):
        '''
        Adds values into tables given the columns
        '''
        # connecting with db
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cols = ""
        for i in range(len(columns)):
            if i != len(columns)-1:
                cols += "'%s', " % columns[i]
            else:
                cols += "'%s'" % columns[i]

        vals = ""
        for i in range(len(values)):
            if i != len(str(values))-1:
                vals += "'%s', " % values[i]
            else:
                vals += "'%s'" % values[i]
        vals = vals[:-2]

        sql_command = "INSERT INTO %s (%s) VALUES (%s)" % (db_table, cols, vals)
        print(sql_command)
        
        cursor.execute(sql_command)
        connection.commit()
        connection.close()
        return 0


    def get_user_info(self, db_name, db_table, email):
        '''
        returns all the stored information about the user in the db as a list
        '''
        connect = sqlite3.connect(db_name)
        cursor = connect.execute("SELECT * FROM %s WHERE Email == '%s'" % (db_table, email))
        user_info = []
        for i in cursor:
            for item in i:
                user_info.append(item)

        return user_info

    def update_user_profile(self, db_name, db_table, email, cols, vals):
        '''
        updates column values given an email and values
        '''
        connect = sqlite3.connect("db.db")
        command = "UPDATE %s SET " % (db_table)
        for i in range(len(cols)):
            if i != (len(cols)-1):
                command += "%s = '%s', " % (cols[i], vals[i])
            else:
                command += "%s = '%s' " % (cols[i], vals[i])

        command += "WHERE Email == '%s';" % (email)
        print(command)
        cursor = connect.execute(command)
        return 0