import sqlite3
import wx
import management as m
import management_dlgs as m_dlgs


class ManageParticipants(object):

    def __init__(self, db):
        self._db = db

    def load_participants(self, _frame, _mode, _selection_value):

        # The group or event name selected in the filter drop-down menu
        _requested_name = _selection_value

        if _mode is not "":

            if _mode is "group":

                _request_data = m.s.load_groups(m.s._id, "load_data")
                _complementary_data = m.e.load_events("load_data")
                _sql_string = '''SELECT * FROM participants WHERE group_id = ?'''

                # index of id of complimentary element in db. Here 2 because the event id is wanted.
                _id_index = 2

            elif _mode is "event":

                _complementary_data = m.s.load_groups(m.s._id, "load_data")
                _request_data = m.e.load_events("load_data")
                _sql_string = '''SELECT * FROM participants WHERE event_id = ?'''

                # index of id of complimentary element in db. Here 1 because the group id is wanted.
                _id_index = 1

            for r in _request_data:
                if _requested_name in r:
                    #group or event id the data was requested for
                    _requested_id = r[0]

            cursor_part = self._db.cursor()
            cursor_part.execute(_sql_string, (str(_requested_id)))
            #tuple with datasets of registrations for the group/event the data was requested for
            _data = cursor_part.fetchall()
            _new_data = []

            for d in _data:
                #group or event id to be exchanged for the name
                _id = d[_id_index]

                for c in _complementary_data:
                    if c[0] is _id:
                        _name = c[1]
                        break
                    else:
                        _name = _id

                # Convert tuple to list, then delete group id and event id and add group/event name
                d_list = list(d)
                d_list.pop(1)
                d_list.pop(1)
                d_list.insert(1,_name)
                d = tuple(d_list)

                _new_data.append(d)

            _data = _new_data

        else:
            _data = []

        # Create a participants object for every dataset
        parts_objects = []
        for p in _data:
            parts_objects.append(Participants(self._db, p))

        # Show the list view window and populate the table.
        if _frame is "":
            _frame = m_dlgs.ListWindow(None, "Participants", "participants")

        #If a frame exists (i.e. the data for the table view is reloaded) just populate the table.
        _frame._display_participants(_data, parts_objects, _requested_name, _mode)

class Participants(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list

    # Dialog window for editing and adding participants data
    def _dialog(self, _dialog_mode, _requested_name, _participants_mode):

        _list_mode = "participants"

        dlg = m_dlgs.DetailWindow(None, "", _dialog_mode, _list_mode)

        if _dialog_mode == "edit":
            # Populate form with existing data
            dlg._edit_participants(self._list, _requested_name, _participants_mode)

        # Show dialog window and retrieve entered values if user pressed OK
        if dlg.ShowModal() == wx.ID_OK:

            # If the id field hasn't been populated before (i.e. a new entry is created), leave it blank.
            # Else, process it as integer.
            if dlg._idField.GetValue() == "":
                _id = ""
            else:
                _id = int(dlg._idField.GetValue())

            _event_selection = dlg._eventChoiceField.GetSelection()
            _event_string = dlg._eventChoiceField.GetString(_event_selection)
            _group_selection = dlg._groupChoiceField.GetSelection()
            _group_string = dlg._groupChoiceField.GetString(_group_selection)

            _groups_data = m.s.load_groups(m.s._id, "load_data")
            _events_data = m.e.load_events("load_data")
            _data_lists =  [_groups_data, _events_data]
            _group_id = ""
            _event_id = ""

            # Convert selected group and event names back to ids
            for d in _data_lists:
                for item in d:

                    if item[1] == _group_string:
                        _group_id = item[0]
                        break

                    elif item[1] == _event_string:
                        _event_id = item[0]
                        break

            _new_data = (
                _id,
                _group_id,
                _event_id,
                dlg._normalParticipantsField.GetValue(),
                dlg._reducedParticipantsField.GetValue(),
                )

            if _dialog_mode == "edit":
                self._update(self._list, _new_data)
            elif _dialog_mode == "new":
                self._new(_new_data)

            return True

        dlg.Destroy()

    def _delete(self):

        # Promt the user with confirmation window.
        dlg = wx.MessageDialog(None, message = "Are you sure you want to delete this registration?",
                                caption = "Delete Registration", style = wx.YES_NO, pos = wx.DefaultPosition)

        if dlg.ShowModal() == wx.ID_YES:
            cursor_delete = self._db.cursor()
            cursor_delete.execute('''DELETE FROM participants WHERE id = ?''', (self._list[0], ))

            self._db.commit()
            return True

        dlg.Destroy()


    def _update(self, _list, _new_data):

        if _list != _new_data:

            cursor_update = self._db.cursor()
            cursor_update.execute('''UPDATE participants SET group_id = ?, event_id = ?, normal_participants = ?, reduced_participants =? WHERE id = ? ''',
            (_new_data[1], _new_data[2], _new_data[3], _new_data[4], _list[0]))

            self._db.commit()

    def _new(self, _new_data):


        cursor_new = self._db.cursor()
        cursor_new.execute('''INSERT INTO participants(group_id, event_id, normal_participants, reduced_participants) VALUES (?,?,?,?);''',
        (_new_data[1], _new_data[2], _new_data[3], _new_data[4]))

        self._db.commit()


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/app.db')

p = ManageParticipants(db)
