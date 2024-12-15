import sqlite3

username = input("Enter username: ")
connection = sqlite3.connect("database.db")
cursor = connection.cursor()

# Parameterized query to prevent SQL injection
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
