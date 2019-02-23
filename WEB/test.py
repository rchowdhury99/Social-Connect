import sqlite3

db_table = "CLIENTS"
email = "john.doe@example.com"
connect = sqlite3.connect("db.db")
cursor = connect.execute("SELECT Email, FacebookID, TwitterID, InstagramID, SnapchatID FROM %s WHERE Email == '%s'" % (db_table, email))
social_links = []
# getting the social links from the query
for i in cursor:
    print(i)
    for item in i:
        if (item.encode("ascii")).decode("utf-8") != email:
            social_links.append((item.encode("ascii")).decode("utf-8"))

print(social_links)
