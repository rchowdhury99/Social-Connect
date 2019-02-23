import sqlite3

db_table = "CLIENTS"
email = "john.doe@example.com"
connect = sqlite3.connect("db.db")

data = {'email': 'faheem5948@gmail.com', 'password': 'sdfghjk', 'facebook_link': 'somelink.com/user-name', 'instagram_link': 'somelink.com/user-name', 'twitter_link': 'somelink.com/user-name', 'snapchat_link': 'somelink.com/user-name'}
command = "INSERT INTO %s (" % (db_table)
for i in range(len(data)):
    if i != len(data)-1:
        print(i)
        print(data[i])
        command += data[i] + ", "
    else:
        command += data[i] + ") VALUES ( "

for i in range(len(data)):
    if i != len(data)-1:
        command += "'" + data[i][i] + "', "
    else:
        command +=  "'" + data[i][i] + "');"

print(command)
