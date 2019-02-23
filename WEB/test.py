import sqlite3

db_table = "CLIENTS"
email = "john.doe@example.com"
connect = sqlite3.connect("db.db")
cursor = connect.execute("SELECT Email, FirstName, LastName FROM %s WHERE Email == '%s' " % (db_table, email))
info = []
for i in cursor:
    for item in i:
        if (item.encode("ascii")).decode("utf-8") != email:
            info.append((item.encode("ascii")).decode("utf-8"))


print(info)
