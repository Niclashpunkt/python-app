
# Prototype of a Python Desktop Application
# Build for the course Tech Basics in the Major Digital Media at Leuphana University
# By Niclas Hedemann

import sqlite3
import wx
import management_dlgs as m_dlgs

class Supergroups(object):

    def __init__(self, db, id):
        self._db = db
        self._id = id
        print("Supergroups init!")
        # self.load_groups(self._id)

    def load_groups(self, _id):

        # Get datasets of all groups from database
        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        # Create a groups object for every dataset
        groups_objects = []
        for g in groups_data:
            groups_objects.append(Groups(self._db, g))

        # Show the groups list view window and populate the table.
        # frame = EntryWindow(None, "")
        frame = m_dlgs.ListWindow(None, "", "groups")
        frame._display_groups(groups_data, groups_objects, self)

    def refresh_groups(self, _id, _frame):

        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        groups_objects = []
        for g in groups_data:
            groups_objects.append(Groups(self._db, g))

        _frame._display_groups(groups_data, groups_objects, self)

class Groups(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list

    # Dialog window for editing and adding group data
    def _dialog(self, _dialog_mode, supergroup_id):

        _list_mode = "groups"

        dlg = m_dlgs.DetailWindow(None, "", _dialog_mode, _list_mode)

        if _dialog_mode == "edit":
            # Populate form with existing data
            dlg._edit_group(self._list)
            _supergroup_id = self._list[2]

        elif _dialog_mode == "new":
            _supergroup_id = supergroup_id

        # Show dialog window and retrieve entered values if user pressed OK
        if dlg.ShowModal() == wx.ID_OK:

            _selection = dlg._gradeField.GetSelection()
            _value = dlg._gradeField.GetValue()

            # If user typed in grade dropdown to select an option, the selection returns -1.
            # In this case, retrieve the field value. But only if it is numeric. Else, set the grade to 7, i.e. "other"
            if _selection == -1 and _value.isdigit():
                if int(_value) < 7:
                    _grade = _value
                else:
                    _grade = 7
            elif _selection == -1 and _value.isalpha():
                _grade = 7
            else:
                _grade = _selection+1

            # If the id field hasn't been populated before (i.e. a new group is created), leave it blank.
            # Else, process it as integer.
            if dlg._idField.GetValue() == "":
                _id = ""
            else:
                _id = int(dlg._idField.GetValue())

            _new_data = (
                _id,
                dlg._nameField.GetValue(),
                _supergroup_id,
                dlg._leaderField.GetValue(),
                _grade)

            if _dialog_mode == "edit":
                self._update(self._list, _new_data)
            elif _dialog_mode == "new":
                self._new(_new_data)

            return True

        dlg.Destroy()

    def _delete(self):

        # Promt the user with confirmation window.
        dlg = wx.MessageDialog(None, message = "Are you sure you want to delete the group "+self._list[1]+" ?",
                                caption = "Delete Group", style = wx.YES_NO, pos = wx.DefaultPosition)

        if dlg.ShowModal() == wx.ID_YES:
            cursor_delete = self._db.cursor()
            cursor_delete.execute('''DELETE FROM groups WHERE id = ?''', (self._list[0], ))

            self._db.commit()
            return True

        dlg.Destroy()


    def _update(self, _list, _new_data):

        if _list != _new_data:

            cursor_update = self._db.cursor()
            cursor_update.execute('''UPDATE groups SET name = ?, leader = ?, grade = ? WHERE id = ? ''',
            (_new_data[1], _new_data[3], _new_data[4], _list[0]))

            self._db.commit()

    def _new(self, _new_data):

        cursor_new = self._db.cursor()
        cursor_new.execute('''INSERT INTO groups(name, super_group_id, leader, grade) VALUES (?,?,?,?);''',
        (_new_data[1], _new_data[2], _new_data[3], _new_data[4]))

        self._db.commit()

class ManageEvents(object):

    def __init__(self, db):
        self._db = db
        print("Events init!")
        # self.load_groups(self._id)

    def load_events(self):

        # Get datasets of all groups from database
        cursor_events = self._db.cursor()
        cursor_events.execute('''SELECT * FROM events''')
        _data = cursor_events.fetchall()

        # Create a events object for every dataset
        events_objects = []
        for e in _data:
            events_objects.append(Events(self._db, e))

        # Show the list view window and populate the table.
        # frame = EntryWindow(None, "")
        frame = m_dlgs.ListWindow(None, "", "events")
        frame._display_events(_data, events_objects)

    def refresh_events(self, _frame):

        cursor_events = self._db.cursor()
        cursor_events.execute('''SELECT * FROM events''')
        _data = cursor_events.fetchall()

        events_objects = []
        for e in _data:
            events_objects.append(Events(self._db, e))

        _frame._display_events(_data, events_objects)

class Events(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list

    # Dialog window for editing and adding events data
    def _dialog(self, _dialog_mode):

        _list_mode = "events"

        dlg = m_dlgs.DetailWindow(None, "", _dialog_mode, _list_mode)

        if _dialog_mode == "edit":
            # Populate form with existing data
            dlg._edit_event(self._list)

        # Show dialog window and retrieve entered values if user pressed OK
        if dlg.ShowModal() == wx.ID_OK:

            # If the id field hasn't been populated before (i.e. a new event is created), leave it blank.
            # Else, process it as integer.
            if dlg._idField.GetValue() == "":
                _id = ""
            else:
                _id = int(dlg._idField.GetValue())

            _new_data = (
                _id,
                dlg._nameField.GetValue(),
                dlg._dateField.GetValue(),
                dlg._normalFeeField.GetValue(),
                dlg._reducedFeeField.GetValue(),
                )

            if _dialog_mode == "edit":
                self._update(self._list, _new_data)
            elif _dialog_mode == "new":
                self._new(_new_data)

            return True

        dlg.Destroy()

    def _delete(self):

        # Promt the user with confirmation window.
        dlg = wx.MessageDialog(None, message = "Are you sure you want to delete the event "+self._list[1]+" ?",
                                caption = "Delete event", style = wx.YES_NO, pos = wx.DefaultPosition)

        if dlg.ShowModal() == wx.ID_YES:
            cursor_delete = self._db.cursor()
            cursor_delete.execute('''DELETE FROM events WHERE id = ?''', (self._list[0], ))

            self._db.commit()
            return True

        dlg.Destroy()


    def _update(self, _list, _new_data):

        if _list != _new_data:

            cursor_update = self._db.cursor()
            cursor_update.execute('''UPDATE events SET name = ?, date = ?, normal_fee = ?, reduced_fee =? WHERE id = ? ''',
            (_new_data[1], _new_data[2], _new_data[3], _new_data[4], _list[0]))

            self._db.commit()

    def _new(self, _new_data):


        cursor_new = self._db.cursor()
        cursor_new.execute('''INSERT INTO events(name, date, normal_fee, reduced_fee) VALUES (?,?,?,?);''',
        (_new_data[1], _new_data[2], _new_data[3], _new_data[4]))

        self._db.commit()


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')

s = Supergroups(db, 1) #requires database object and the id of the supergroup.
e = ManageEvents(db) #requires database object and the id of the supergroup.

# # As of now, the id is hardcoded, as the app only deals with one supergroup.
