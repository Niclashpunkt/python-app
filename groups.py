import sqlite3

class Supergroups(object):

    def __init__(self, db, id):
        self._db = db
        self._id = id
        self.load_groups(self._id)

    def load_groups(self, _id):

        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        groups_list = []
        for g in groups_data:
            print(g)
            groups_list.append(Groups(self._db, g))
        print(groups_list)



class Groups(object):

    def __init__(self, db, data):
        self._db = db
        self._data = data
        print(self._data[1])


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')

s = Supergroups(db, 1)
