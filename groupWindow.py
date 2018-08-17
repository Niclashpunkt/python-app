import sys
import random

import pyforms
from pyforms            import BaseWidget
from pyforms.controls   import ControlText
from pyforms.controls   import ControlButton
from pyforms.controls   import ControlNumber
from pyforms.controls   import ControlCombo

class createId(object):

    def random(type):

        if type is "group":
            prefix = "g"

        elif type is "super":
            prefix = "s"

        else:
            sys.exit("Error: ID request was for neither a group nor a super group.")

        number = random.randint(1,100)

        if number < 100 and number > 9:
            number = "0" + str(number)
        elif number < 10:
            number = "00" + str(number)
        else:
            number = str(number)

        id = prefix + number
        return id

class groupWindow(BaseWidget):

    def __init__(self):
        super(groupWindow,self).__init__('Add Group')

        #Definition of form fields
        self._idField = ControlText("ID")
        self._idField.value = createId.random("group")      # Either "group" or "super"
        self._idField.enabled = False

        self._nameField = ControlText("Group Name")
        self._leaderField = ControlText("Group Leader")

        self._superGroupField = ControlCombo("Super Group")
        self._superGroupField.add_item('Dietrich von Bern', 'dvb')
        self._superGroupField.add_item('Andwaranaut', '')

        self._gradeField = ControlCombo("Grade")
        self._gradeField.add_item('1', '1')
        self._gradeField.add_item('2')
        self._gradeField.add_item('3')
        self._gradeField.add_item('4')
        self._gradeField.add_item('5')
        self._gradeField.add_item('6')
        self._gradeField.add_item('other', '7')

        self._submitBtn = ControlButton('Submit')

#Execute the application
if __name__ == "__main__":   pyforms.start_app( groupWindow )
