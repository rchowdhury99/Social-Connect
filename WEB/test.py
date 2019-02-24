import sqlite3

db_name = "db.db"
db_table = "CLIENTS"
email = "john.doe@example.com"
connect = sqlite3.connect(db_name)
cursor = connect.execute("SELECT * FROM %s WHERE Email == '%s'" % (db_table, email))
user_info = []
for i in cursor:
    for item in i:
        user_info.append(item)

print(user_info)