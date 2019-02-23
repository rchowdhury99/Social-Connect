import sqlite3

connection = sqlite3.connect("db.db")
x = connection.execute("SELECT Email, Password FROM CLIENTS WHERE Email == 'john.doe@example.com'");
password = None
for i in x:
    print(i)
    password = list(i)
    password.remove("john.doe@example.com")
print(password)
