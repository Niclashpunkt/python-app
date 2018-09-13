import sqlite3

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE groups(id INTEGER PRIMARY KEY, name TEXT, super_group_id INTEGER, leader TEXT, grade INTEGER)
''')
db.commit()
