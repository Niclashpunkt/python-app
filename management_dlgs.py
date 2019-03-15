import sqlite3
import wx
import management as m

# The dialog where the user can edit or create group data
class DetailWindow(wx.Dialog):
    def __init__(self, parent, title, dialog_mode, list_mode):

        _dialog_mode = dialog_mode
        _list_mode = list_mode

        if _dialog_mode is "edit" and _list_mode is "groups":
            _title = "Edit Group Data"
        elif _dialog_mode is "new" and _list_mode is "groups":
            _title = "Enter a New Group"
        elif _dialog_mode is "edit" and _list_mode is "events":
            _title = "Edit Event Data"
        elif _dialog_mode is "new" and _list_mode is "events":
            _title = "Enter a New Event"

        wx.Dialog.__init__(self, parent, title=_title, size=(300,225))

        _label_margin = 5
        _ctrl_margin = 75
        _ctrl_offset_list = []
        _label_offset_list = []
        for row in range(0,7):
            _ctrl_offset = 20 + 20*row + 3*row
            _label_offset = _ctrl_offset + 3
            _ctrl_offset_list.append(_ctrl_offset)
            _label_offset_list.append(_label_offset)

        if _list_mode is "groups":

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

        elif _list_mode is "events":

            # Create labels
            self._idLabel = wx.StaticText(self, wx.ID_ANY, 'Event ID',    (_label_margin,_label_offset_list[0]))
            self._nameLabel = wx.StaticText(self, wx.ID_ANY, 'Name',  (_label_margin,_label_offset_list[1]))
            self._dateLabel = wx.StaticText(self, wx.ID_ANY, 'Date',  (_label_margin,_label_offset_list[2]))
            self._normalFeeLabel = wx.StaticText(self, wx.ID_ANY, 'Normal Fee',  (_label_margin,_label_offset_list[3]))
            self._reducedFeeLabel = wx.StaticText(self, wx.ID_ANY, 'Reduced Fee',  (_label_margin,_label_offset_list[4]))

            # Create empty form fields
            self._idField = wx.TextCtrl(self,wx.ID_ANY, "",    (_ctrl_margin,_ctrl_offset_list[0]), (20,20), style=wx.TE_READONLY)
            self._nameField = wx.TextCtrl(self,wx.ID_ANY, "",   (_ctrl_margin,_ctrl_offset_list[1]))
            self._dateField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[2]))
            self._normalFeeField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[3]))
            self._reducedFeeField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[4]))

            self._submitBtn = wx.Button(self, wx.ID_OK, "&Save", (_label_margin,_ctrl_offset_list[6]))
            self._exitBtn = wx.Button(self, wx.ID_CANCEL , "&Cancel", (_ctrl_margin + _label_margin*6,_ctrl_offset_list[6]))

    def _edit_group(self, _data):

        self.dialog_mode = "edit"

        # Populate form fields with data to edit.
        self._idField.SetValue(str(_data[0]))
        self._nameField.SetValue(_data[1])
        self._leaderField.SetValue(_data[3])
        self._gradeField.SetSelection(_data[4] - 1)

    def _edit_event(self, _data):

        self.dialog_mode = "edit"

        # Populate form fields with data to edit.
        self._idField.SetValue(str(_data[0]))
        self._nameField.SetValue(_data[1])
        self._dateField.SetValue(_data[2])
        self._normalFeeField.SetValue(_data[3])
        self._reducedFeeField.SetValue(_data[4])

# Window with table view of all groups in specified supergroup.
class ListWindow(wx.Frame):
    def __init__(self, parent, title, list_mode):

        _title = "Groups in Supergroup"
        _list_mode = list_mode



        if _list_mode is "groups":

            wx.Frame.__init__(self, parent, title=_title, size=(500,300))
            panel = wx.Panel(self, -1)

            _subject = "Group"

            # Create table and add columns.
            self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
            self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=40)
            self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Leader", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Grade", format=wx.LIST_FORMAT_LEFT, width=60)

        elif _list_mode is "events":

            wx.Frame.__init__(self, parent, title=_title, size=(500,300))
            panel = wx.Panel(self, -1)

            _subject = "Event"

            # Create table and add columns.
            self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
            self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=40)
            self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Date", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Normal Fee", format=wx.LIST_FORMAT_LEFT, width=60)
            self._listCtrl.AppendColumn("Reduced Fee", format=wx.LIST_FORMAT_LEFT, width=60)

        # Create group management buttons.
        self._editBtn = wx.Button(panel, wx.ID_ANY, "&Edit Selected", (-1,-1))
        self._createBtn = wx.Button(panel, wx.ID_ANY, "Create &New " + _subject, (-1,-1))
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
        panel_sizer.Add(list_sizer, 2, wx.ALL | wx.EXPAND, 5)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(vline, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(tools_sizer, 0,wx.ALL, 5)

        # panel_sizer.SetSizeHints(panel)
        panel.SetSizer(panel_sizer)
        panel.SetAutoLayout(1)
        panel_sizer.Fit(self)

    # Populate group table from database
    def _display_groups(self, _data, _data_objects, _supergroup):

        # Bind ui button events to functions
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=_supergroup, _edit_mode="group": self._edit_selected(event, _data_objects, _supergroup, _edit_mode))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=_supergroup, _creation_mode="group": self._create(event, _supergroup, _creation_mode))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=_supergroup, _delete_mode="group": self._delete(event, _data_objects, _supergroup, _delete_mode))

        # self._reportBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list: self._report(event, _groups_list))

        for g in _data:

            _index = self._listCtrl.InsertItem(0, str(g[0]))
            self._listCtrl.SetItem(_index, 1, str(g[1]))
            self._listCtrl.SetItem(_index, 2, str(g[3]))

            if g[4] == 7:
                self._listCtrl.SetItem(_index, 3, "Other")
            else:
                self._listCtrl.SetItem(_index, 3, str(g[4]))

        self.Show()

    def _display_events(self, _data, _data_objects):

        # Bind ui button events to functions
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _edit_mode="event": self._edit_selected(event, _data_objects, _supergroup, _edit_mode))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=0, _creation_mode="event": self._create(event, _supergroup, _creation_mode))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _delete_mode="event": self._delete(event, _data_objects, _supergroup, _delete_mode))

        # self._reportBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list: self._report(event, _groups_list))

        for e in _data:

            _index = self._listCtrl.InsertItem(0, str(e[0]))
            self._listCtrl.SetItem(_index, 1, str(e[1]))
            self._listCtrl.SetItem(_index, 2, str(e[2]))
            self._listCtrl.SetItem(_index, 3, str(e[3]))
            self._listCtrl.SetItem(_index, 4, str(e[4]))

        self.Show()

    def _edit_selected(self, event, _data_objects, _supergroup, _edit_mode):

        _selection = self._listCtrl.GetFirstSelected()

        # Get selected entry and call the edit dialog of its object.
        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():

            # Get id value of selection
            _selected_id = self._listCtrl.GetItemText(_selection)

            i = 0
            # Look for this id in list of objects
            for d in _data_objects:

                if  _data_objects[i]._list[0] == int(_selected_id):
                    entry_to_edit = d
                i += 1

            # If edit dialog was successful, refresh table.
            if _edit_mode is "group":
                if entry_to_edit._dialog("edit", _supergroup._id) is True:
                    self._listCtrl.DeleteAllItems()
                    _supergroup.refresh_groups(_supergroup._id, self)

            elif _edit_mode is "event":
                if entry_to_edit._dialog("edit") is True:
                    print("event edit succcessful")
                    self._listCtrl.DeleteAllItems()
                    m.e.refresh_events(self)

    def _delete(self, event, _data_list, _supergroup, _delete_mode):

        _selection = self._listCtrl.GetFirstSelected()

        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():
            _selected_id = self._listCtrl.GetItemText(_selection)

            i = 0
            for d in _data_list:

                if _data_list[i]._list[0] == int(_selected_id):
                    entry_to_delete = d
                i += 1

            if entry_to_delete._delete() is True:
                self._listCtrl.DeleteAllItems()
                if _delete_mode is "group":
                    _supergroup.refresh_groups(_supergroup._id, self)
                elif _delete_mode is "event":
                    m.e.refresh_events(self)


    def _create(self, event, _supergroup, _creation_mode):
        if _creation_mode is "group":
            c = m.Groups(m.db, "")

            if c._dialog("new", _supergroup._id) is True:
                self._listCtrl.DeleteAllItems()
                _supergroup.refresh_groups(_supergroup._id, self)

        elif _creation_mode is "event":
            c = m.Events(m.db, "")

            if c._dialog("new") is True:
                self._listCtrl.DeleteAllItems()
                m.e.refresh_events(self)
                print("refreshed events!")
