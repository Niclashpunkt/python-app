import sys
import random

import sqlite3

import pyforms
from pyforms            import BaseWidget
from pyforms.controls   import ControlText
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlNumber
from pyforms.controls   import ControlCombo

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb')

class GroupWindow(BaseWidget):

    def __init__(self):
        super(groupWindow,self).__init__('Add Group')

        #Definition of form fields
        self._idField = ControlText("ID")
        # self._idField.value = createId.random("group")         # Either "group" or "super"
        self._idField.enabled = False

        self._nameField = ControlText("Group Name")
        self._leaderField = ControlText("Group Leader")

        self._superGroupField = ControlCombo("Super Group")
        # self._superGroupField.add_item('Dietrich von Bern', 'dvb')
        # self._superGroupField.add_item('Andwaranaut', '')

        cursor_super = db.cursor()
        cursor_super.execute('''
            SELECT id, name FROM supergroups;
        ''')
        supergroup_data = cursor_super.fetchall()

        for row in supergroup_data:
            self._superGroupField.add_item(row[1], row[0])

        self._gradeField = ControlCombo("Grade")
        self._gradeField.add_item('1', '1')
        self._gradeField.add_item('2')
        self._gradeField.add_item('3')
        self._gradeField.add_item('4')
        self._gradeField.add_item('5')
        self._gradeField.add_item('6')
        self._gradeField.add_item('other', '7')

        self._submitBtn = ControlButton('Submit')
        self._submitBtn.value = self.update

        # Fill form with existing data
        cursor_group = db.cursor()
        cursor_group.execute('''
            SELECT id, name, leader, super_group_id, grade FROM groups WHERE id = 1;
        ''')
        group_data = cursor_group.fetchone()

        self._idField.value = str(group_data[0])
        self._nameField.value = str(group_data[1])
        self._leaderField.value = str(group_data[2])
        self._superGroupField.value = str(group_data[3])
        self._gradeField.value = str(group_data[4])


        # def update(self):
        #     self.



#Execute the application
if __name__ == "__main__":   pyforms.start_app( groupWindow )
