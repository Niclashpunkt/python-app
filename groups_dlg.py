import sqlite3
import wx

class Supergroups(object):

    def __init__(self, db, id):
        self._db = db
        self._id = id
        self.load_groups(self._id)

    def load_groups(self, _id):

        # Get datasets of all groups from database
        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        # Create a groups object for every dataset
        groups_list = []
        for g in groups_data:
            groups_list.append(Groups(self._db, g))

        # Show the groups list view window and populate the table.
        frame = GroupListWindow(None, "")
        frame._display_groups(groups_data, groups_list, self)

    def refresh_groups(self, _id, _frame):

        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        groups_list = []
        for g in groups_data:
            groups_list.append(Groups(self._db, g))

        _frame._display_groups(groups_data, groups_list, self)

class Groups(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list

    # Dialog window for editing and adding group data
    def _dialog(self, _dialog_mode, supergroup_id):

        dlg = GroupWindow(None, "", _dialog_mode)

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
            cursor_delete.execute('''DELETE FROM groups WHERE id = ?''', str((self._list[0])))

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

# The dialog where the user can edit or create group data
class GroupWindow(wx.Dialog):
    def __init__(self, parent, title, dialog_mode):

        _dialog_mode = dialog_mode

        if _dialog_mode is "edit":
            _title = "Edit Group Data"
        elif _dialog_mode is "new":
            _title = "Enter a New Group"

        wx.Dialog.__init__(self, parent, title=_title, size=(300,225))

        _label_margin = 5
        _ctrl_margin = 75
        _ctrl_offset_list = []
        _label_offset_list = []
        for row in range(0,6):
            _ctrl_offset = 20 + 20*row + 3*row
            _label_offset = _ctrl_offset + 3
            _ctrl_offset_list.append(_ctrl_offset)
            _label_offset_list.append(_label_offset)

        # Create labels
        self._idLabel = wx.StaticText(self, wx.ID_ANY, 'Group ID',    (_label_margin,_label_offset_list[0]))
        self._nameLabel = wx.StaticText(self, wx.ID_ANY, 'Name',  (_label_margin,_label_offset_list[1]))
        self._leaderLabel = wx.StaticText(self, wx.ID_ANY, 'Leader',  (_label_margin,_label_offset_list[2]))
        self._gradeLabel = wx.StaticText(self, wx.ID_ANY, 'Grade',  (_label_margin,_label_offset_list[3]))

        # Create empty form fields
        self._idField = wx.TextCtrl(self,wx.ID_ANY, "",    (_ctrl_margin,_ctrl_offset_list[0]), (20,20), style=wx.TE_READONLY)
        self._nameField = wx.TextCtrl(self,wx.ID_ANY, "",   (_ctrl_margin,_ctrl_offset_list[1]))
        self._leaderField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[2]))
        self._gradeField = wx.ComboBox(self, wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[3]), choices=['1','2','3','4','5','6','Other'], style=0)
        self._gradeField.SetSelection(0)
        self._submitBtn = wx.Button(self, wx.ID_OK, "&Save", (_label_margin,_ctrl_offset_list[5]))
        self._exitBtn = wx.Button(self, wx.ID_CANCEL , "&Cancel", (_ctrl_margin + _label_margin*6,_ctrl_offset_list[5]))

    def _edit_group(self, _data):

        self.dialog_mode = "edit"

        # Populate form fields with data to edit.
        self._idField.SetValue(str(_data[0]))
        self._nameField.SetValue(_data[1])
        self._leaderField.SetValue(_data[3])
        self._gradeField.SetSelection(_data[4] - 1)

# Window with table view of all groups in specified supergroup.
class GroupListWindow(wx.Frame):
    def __init__(self, parent, title):

        _title = "Groups in Supergroup"
        wx.Frame.__init__(self, parent, title=_title, size=(500,300))
        panel = wx.Panel(self, -1)

        _margin = 5

        # Create table and add columns.
        self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
        self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=40)
        self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
        self._listCtrl.AppendColumn("Leader", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
        self._listCtrl.AppendColumn("Grade", format=wx.LIST_FORMAT_LEFT, width=60)

        # Create group management buttons.
        self._editBtn = wx.Button(panel, wx.ID_ANY, "&Edit Selected", (-1,-1))
        self._createBtn = wx.Button(panel, wx.ID_ANY, "Create &New Group", (-1,-1))
        self._deleteBtn = wx.Button(panel, wx.ID_ANY, "&Delete Selected", (-1,-1))

        vline = wx.StaticLine(panel, wx.ID_ANY, (-1,-1), (-1,-1), style=wx.LI_VERTICAL)

        self._reportBtn = wx.Button(panel, wx.ID_ANY, "E&xport List")

        # Organize group buttons horizontally.
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self._editBtn, 1, wx.EXPAND)
        btn_sizer.Add(self._createBtn, 1, wx.EXPAND | wx.LEFT, 5)
        btn_sizer.Add(self._deleteBtn, 1, wx.EXPAND | wx.LEFT, 5)

        # Group table and group buttons.
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(self._listCtrl, 1, wx.EXPAND | wx.BOTTOM, 5)
        list_sizer.Add(btn_sizer, 0, wx.BOTTOM, 5)

        tools_sizer = wx.BoxSizer(wx.VERTICAL)
        tools_sizer.Add(self._reportBtn, 1, wx.EXPAND)

        # Lay out group view sizer and sidebar horizontally.
        panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel_sizer.Add(list_sizer, 1, wx.ALL | wx.EXPAND, 5)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(vline, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(tools_sizer, 0,wx.ALL, 5)

        panel.SetSizer(panel_sizer)
        panel.SetAutoLayout(1)
        panel_sizer.Fit(self)

    # Populate group table from database
    def _display_groups(self, _groups_data, _groups_list, _supergroup):

        # Bind ui button events to functions
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list, _supergroup=_supergroup: self._edit_selected(event, _groups_list, _supergroup))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=_supergroup: self._create(event, _supergroup))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list, _supergroup=_supergroup: self._delete(event, _groups_list, _supergroup))

        # self._reportBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list: self._report(event, _groups_list))


        for g in _groups_data:

            _index = self._listCtrl.InsertItem(0, str(g[0]))
            # print(g[0])
            self._listCtrl.SetItem(_index, 1, str(g[1]))
            self._listCtrl.SetItem(_index, 2, str(g[3]))

            if g[4] == 7:
                self._listCtrl.SetItem(_index, 3, "Other")
            else:
                self._listCtrl.SetItem(_index, 3, str(g[4]))

        self.Show()

    def _edit_selected(self, event, _groups_list, _supergroup):

        _selection = self._listCtrl.GetFirstSelected()

        # Get selected group and call the edit dialog of its object.
        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():

            # Get id value of selection
            _selected_id = self._listCtrl.GetItemText(_selection)

            i = 0
            # Look for this id in list of group objects
            for g in _groups_list:

                if _groups_list[i]._list[0] == int(_selected_id):
                    group_to_edit = g
                i += 1

            # If edit dialog of group was successful, refresh table.
            if group_to_edit._dialog("edit", _supergroup._id) is True:
                self._listCtrl.DeleteAllItems()
                _supergroup.refresh_groups(_supergroup._id, self)

    def _delete(self, event, _groups_list, _supergroup):

        _selection = self._listCtrl.GetFirstSelected()

        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():
            _selected_id = self._listCtrl.GetItemText(_selection)

            i = 0
            for g in _groups_list:

                if _groups_list[i]._list[0] == int(_selected_id):
                    group_to_delete = g
                i += 1

            if group_to_delete._delete() is True:
                self._listCtrl.DeleteAllItems()
                _supergroup.refresh_groups(_supergroup._id, self)


    def _create(self, event, _supergroup):
        g = Groups(db, "")
        if g._dialog("new", _supergroup._id) is True:
            self._listCtrl.DeleteAllItems()
            _supergroup.refresh_groups(_supergroup._id, self)


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')


app = wx.App(False)
s = Supergroups(db, 1) #requires database object and the id of the supergroup.
# As of now, the id is hardcoded, as the app only deals with one supergroup.

app.MainLoop()
