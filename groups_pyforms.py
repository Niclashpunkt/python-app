import sqlite3

import pyforms
from pyforms            import BaseWidget
from pyforms.controls   import ControlText
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlNumber
from pyforms.controls   import ControlCombo
from pyforms.controls   import ControlEmptyWidget
from pyforms.controls   import ControlList
from pyforms.controls   import ControlLabel
from pyforms.controls   import ControlEmptyWidget

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

        g0 = groups_list[0]
        w = g0.edit(g0)

        return groups_data

        # win = GroupsListWindow(self._db, groups_data)
        # win.parent = self
        # EmptyWindow._panel.value = win

        # gw = GroupsListWindow(self._db, groups_data)



class Groups(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list
        print(self._list[1])

    def edit(self, _list):

        win = GroupWindow(_list)
        win.parent = self
        win.show()

# class EmptyWindow(BaseWidget):
#     def __init__(self):
#         BaseWidget.__init__(self,'Empty window')
#         self._lable = ControlLabel('Empty!')
#         self._panel = ControlEmptyWidget()

class GroupWindow(BaseWidget):

    def __init__(self, list):
        BaseWidget.__init__(self,'Groups window')

        self._list = list

        #Definition of form fields
        self._idField = ControlText("ID")
        self._idField.enabled = False

        self._nameField = ControlText("Group Name")
        self._leaderField = ControlText("Group Leader")

        self._gradeField = ControlCombo("Grade")
        self._gradeField.add_item('1', '1')
        self._gradeField.add_item('2')
        self._gradeField.add_item('3')
        self._gradeField.add_item('4')
        self._gradeField.add_item('5')
        self._gradeField.add_item('6')
        self._gradeField.add_item('other', '7')

        self._submitBtn = ControlButton('Submit')
        # self._submitBtn.value =

    def _edit_group(_list):
        self._idField.value = str(_list[0])
        self._nameField.value = str(_list[1])
        self._leaderField.value = str(_list[2])
        self._gradeField.value = str(_list[4])

class GroupsListWindow(BaseWidget):

    def __init__(self):
        BaseWidget.__init__(self,'Groups List window')

        # self._db = db
        # self._groups_data = groups_data


        #Definition of the forms fields
        self._groupsList    = ControlList('Groups')
        self._groupsList.__add__((1,'Rekkared',1,'Sigils',5))
            # plusFunction    = self.__addPersonBtnAction,
            # minusFunction   = self.__rmPersonBtnAction)

        self._groupsList.horizontal_headers = ['ID', 'Name', 'Super Group ID', 'Leader', 'Grade']
        self._groupsList.readonly = True
        self._groupsList.resize_rows_contents()


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')



# Execute the application
if __name__ == "__main__":   pyforms.start_app( GroupsListWindow )

s = Supergroups(db, 1)
groups_data = s.load_groups

list = s.load_groups
print("S:")
print(list)
