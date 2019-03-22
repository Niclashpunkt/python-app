import sqlite3
import wx

import management as m
import participants as p
import entry as e


# The dialog where the user can edit or create data
class DetailWindow(wx.Dialog):
    def __init__(self, parent, _title, dialog_mode, list_mode):

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
        elif _dialog_mode is "edit" and _list_mode is "participants":
            _title = "Edit Participant Registration"
        elif _dialog_mode is "new" and _list_mode is "participants":
            _title = "Register Participants"

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
            self._exitBtn = wx.Button(self, wx.ID_CANCEL , "&Cancel", (_ctrl_margin + _label_margin*7,_ctrl_offset_list[6]))

        elif _list_mode is "participants":

            group_names = m.s.load_groups(m.s._id, "load_names")
            group_names.sort()
            group_names.insert(0, "No Group Selected")
            event_names = m.e.load_events("load_names")
            event_names.sort()
            event_names.insert(0, "No Event Selected")

            # Create labels
            self._idLabel = wx.StaticText(self, wx.ID_ANY, 'Entry ID',    (_label_margin,_label_offset_list[0]))
            self._eventChoiceLabel = wx.StaticText(self, wx.ID_ANY, 'Event',  (_label_margin,_label_offset_list[1]))
            self._groupChoiceLabel = wx.StaticText(self, wx.ID_ANY, 'Group',  (_label_margin,_label_offset_list[2]))
            self._normalPartiscipantsLabel = wx.StaticText(self, wx.ID_ANY, 'Participants, normal Fee',  (_label_margin,_label_offset_list[3]+4))
            self._reducedParticipantsLabel = wx.StaticText(self, wx.ID_ANY, 'Participants, reduced Fee',  (_label_margin,_label_offset_list[4]+6))

            # Create empty form fields
            self._idField = wx.TextCtrl(self,wx.ID_ANY, "",    (_ctrl_margin,_ctrl_offset_list[0]), (20,20), style=wx.TE_READONLY)
            self._eventChoiceField = wx.Choice(self,wx.ID_ANY, (_ctrl_margin,_ctrl_offset_list[1]), choices=event_names)
            self._groupChoiceField = wx.Choice(self,wx.ID_ANY, (_ctrl_margin,_ctrl_offset_list[2]), choices=group_names)
            self._groupChoiceField.SetSelection(0)
            self._eventChoiceField.SetSelection(0)
            self._normalParticipantsField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin+67,_ctrl_offset_list[3]+4))
            self._reducedParticipantsField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin+67,_ctrl_offset_list[4]+6))

            self._submitBtn = wx.Button(self, wx.ID_OK, "&Save", (_label_margin,_ctrl_offset_list[6]))
            self._exitBtn = wx.Button(self, wx.ID_CANCEL , "&Cancel", (_ctrl_margin + _label_margin*7,_ctrl_offset_list[6]))

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
        self._normalFeeField.SetValue(str(_data[3]))
        self._reducedFeeField.SetValue(str(_data[4]))

    def _edit_participants(self, _data, _requested_name, _participants_mode):

        self.dialog_mode = "edit"

        # Set drop-downs to values from the data set to edit.
        if _participants_mode is "group":
            _group_selection = self._groupChoiceField.FindString(_requested_name)
            self._groupChoiceField.SetSelection(_group_selection)

            _event_selection = self._eventChoiceField.FindString(_data[1])
            self._eventChoiceField.SetSelection(_event_selection)

        elif _participants_mode is "event":
            _event_selection = self._eventChoiceField.FindString(_requested_name)
            self._eventChoiceField.SetSelection(_event_selection)

            _group_selection = self._groupChoiceField.FindString(_data[1])
            self._groupChoiceField.SetSelection(_group_selection)


        # Populate form fields with data to edit.
        self._idField.SetValue(str(_data[0]))
        self._normalParticipantsField.SetValue(str(_data[2]))
        self._reducedParticipantsField.SetValue(str(_data[3]))

# Window with table view of database table entries.
class ListWindow(wx.Frame):
    def __init__(self, parent, title, list_mode):

        _title = title
        _list_mode = list_mode

        top_sizer = wx.BoxSizer(wx.VERTICAL)

        wx.Frame.__init__(self, parent, title=_title, size=(500,300))
        panel = wx.Panel(self, -1)

        self.Bind(wx.EVT_CLOSE, self.on_close)

        if _list_mode is "groups":

            _subject = "Group"

            # Create table and add columns.
            self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
            self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=40)
            self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Leader", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Grade", format=wx.LIST_FORMAT_LEFT, width=60)

        elif _list_mode is "events":

            _subject = "Event"

            # Create table and add columns.
            self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
            self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=40)
            self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Date", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Normal Fee", format=wx.LIST_FORMAT_LEFT, width=60)
            self._listCtrl.AppendColumn("Reduced Fee", format=wx.LIST_FORMAT_LEFT, width=60)

        elif _list_mode is "participants":

            _subject = "Entry"

            group_names = m.s.load_groups(m.s._id, "load_names")
            group_names.sort()
            group_names.insert(0, "No Group Selected")
            event_names = m.e.load_events("load_names")
            event_names.sort()
            event_names.insert(0, "No Event Selected")

            # Create tool bar above list ctrl
            self._staticText = wx.StaticText(panel, wx.NewId(), "Please choose a group or an event and press 'Display Data'.", (-1, -1), wx.DefaultSize)
            self._groupSelectionField = wx.Choice(panel, wx.ID_ANY, choices=group_names)
            self._groupSelectionField.SetSelection(0)
            self._eventSelectionField = wx.Choice(panel, wx.ID_ANY, choices=event_names)
            self._eventSelectionField.SetSelection(0)
            self._displayBtn = wx.Button(panel, wx.ID_ANY, "Displa&y Data", (-1,-1))

            self._groupSelectionField.Bind(wx.EVT_CHOICE, lambda event, choice_ctrl = self._groupSelectionField, other_choice_ctrl = self._eventSelectionField: self._choice_select(event, choice_ctrl, other_choice_ctrl))
            self._eventSelectionField.Bind(wx.EVT_CHOICE, lambda event, choice_ctrl = self._eventSelectionField, other_choice_ctrl = self._groupSelectionField: self._choice_select(event, choice_ctrl, other_choice_ctrl))
            self._displayBtn.Bind(wx.EVT_BUTTON, lambda event: self._load_participants_data())

            # Create table and add columns.
            self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (-1,-1), style=wx.LC_REPORT)
            self._listCtrl.AppendColumn("Entry ID", format=wx.LIST_FORMAT_LEFT, width=60)
            self._listCtrl.AppendColumn("Group/Event", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Normal", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
            self._listCtrl.AppendColumn("Reduced", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)

            # Organize combo boxes horizontally.
            choice_sizer = wx.BoxSizer(wx.HORIZONTAL)
            choice_sizer.Add(self._groupSelectionField, 1, wx.EXPAND)
            choice_sizer.Add(self._eventSelectionField, 1, wx.EXPAND | wx.LEFT, 5)
            choice_sizer.Add(self._displayBtn, 1, wx.EXPAND | wx.LEFT, 5)

            top_sizer.Add(self._staticText, 1, wx.EXPAND)
            top_sizer.Add(choice_sizer, 1, wx.EXPAND)


        # Create management buttons.
        self._editBtn = wx.Button(panel, wx.ID_ANY, "&Edit Selected", (-1,-1))
        self._createBtn = wx.Button(panel, wx.ID_ANY, "Create &New " + _subject, (-1,-1))
        self._deleteBtn = wx.Button(panel, wx.ID_ANY, "&Delete Selected", (-1,-1))

        vline = wx.StaticLine(panel, wx.ID_ANY, (-1,-1), (-1,-1), style=wx.LI_VERTICAL)

        self._menuBtn = wx.Button(panel, wx.ID_ANY, "&Back to Menu")
        self._menuBtn.Bind(wx.EVT_BUTTON, self._menu)

        # Organize group buttons horizontally.
        btn_sizer = wx.BoxSizer(wx.HORIZONTAL)
        btn_sizer.Add(self._editBtn, 1, wx.EXPAND)
        btn_sizer.Add(self._createBtn, 1, wx.EXPAND | wx.LEFT, 5)
        btn_sizer.Add(self._deleteBtn, 1, wx.EXPAND | wx.LEFT, 5)

        # Group table and group buttons.
        list_sizer = wx.BoxSizer(wx.VERTICAL)
        list_sizer.Add(top_sizer, 0, wx.BOTTOM | wx.EXPAND, 5)
        list_sizer.Add(self._listCtrl, 1, wx.EXPAND | wx.BOTTOM, 5)
        list_sizer.Add(btn_sizer, 0, wx.BOTTOM, 5)

        tools_sizer = wx.BoxSizer(wx.VERTICAL)
        tools_sizer.Add(self._menuBtn, 1, wx.EXPAND)

        # Lay out group view sizer and sidebar horizontally.
        panel_sizer = wx.BoxSizer(wx.HORIZONTAL)
        panel_sizer.Add(list_sizer, 2, wx.ALL | wx.EXPAND, 5)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(vline, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 10)
        panel_sizer.Add((5,-1))
        panel_sizer.Add(tools_sizer, 0,wx.ALL, 5)

        panel.SetSizer(panel_sizer)
        panel.SetAutoLayout(1)
        panel_sizer.Fit(self)

    # Populate group table from database
    def _display_groups(self, _data, _data_objects, _supergroup):

        # Bind ui button events to functions
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=_supergroup, _edit_mode="group", _requested_name="", _participants_mode="": self._edit_selected(event, _data_objects, _supergroup, _edit_mode, _requested_name, _participants_mode))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=_supergroup, _creation_mode="group": self._create(event, _supergroup, _creation_mode))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=_supergroup, _delete_mode="group": self._delete(event, _data_objects, _supergroup, _delete_mode))

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
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _edit_mode="event", _requested_name="", _participants_mode="": self._edit_selected(event, _data_objects, _supergroup, _edit_mode, _requested_name, _participants_mode))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=0, _creation_mode="event": self._create(event, _supergroup, _creation_mode))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _delete_mode="event": self._delete(event, _data_objects, _supergroup, _delete_mode))

        for e in _data:

            _index = self._listCtrl.InsertItem(0, str(e[0]))
            self._listCtrl.SetItem(_index, 1, str(e[1]))
            self._listCtrl.SetItem(_index, 2, str(e[2]))
            self._listCtrl.SetItem(_index, 3, str(e[3]))
            self._listCtrl.SetItem(_index, 4, str(e[4]))

        self.Show()

    def _display_participants(self, _data, _data_objects, _requested_name, _participants_mode):

        # Bind ui button events to functions
        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _edit_mode="participants", _requested_name=_requested_name, _participants_mode=_participants_mode: self._edit_selected(event, _data_objects, _supergroup, _edit_mode, _requested_name, _participants_mode))
        self._createBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=0, _creation_mode="participants": self._create(event, _supergroup, _creation_mode))
        self._deleteBtn.Bind(wx.EVT_BUTTON, lambda event, _data_objects=_data_objects, _supergroup=0, _delete_mode="participants": self._delete(event, _data_objects, _supergroup, _delete_mode))

        for p in _data:

            _index = self._listCtrl.InsertItem(0, str(p[0]))
            self._listCtrl.SetItem(_index, 1, str(p[1]))
            self._listCtrl.SetItem(_index, 2, str(p[2]))
            self._listCtrl.SetItem(_index, 3, str(p[3]))

        self.Show()

    def _edit_selected(self, event, _data_objects, _supergroup, _edit_mode, _requested_name, _participants_mode):

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
                    _supergroup.load_groups(_supergroup._id, self)

            elif _edit_mode is "event":
                if entry_to_edit._dialog("edit") is True:
                    self._listCtrl.DeleteAllItems()
                    m.e.load_events(self)

            elif _edit_mode is "participants":
                if entry_to_edit._dialog("edit", _requested_name, _participants_mode) is True:
                    self._listCtrl.DeleteAllItems()
                    self._load_participants_data()

    def _delete(self, event, _data_list, _supergroup, _delete_mode):

        _selection = self._listCtrl.GetFirstSelected()

        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():
            _selected_id = self._listCtrl.GetItemText(_selection)

            i = 0
            for d in _data_list:

                if _data_list[i]._list[0] == int(_selected_id):
                    entry_to_delete = d
                i += 1

            # If delete dialog was successful, refresh table.
            if entry_to_delete._delete() is True:
                self._listCtrl.DeleteAllItems()
                if _delete_mode is "group":
                    _supergroup.load_groups(_supergroup._id, self)
                elif _delete_mode is "event":
                    m.e.load_events(self)
                elif _delete_mode is "participants":
                    self._load_participants_data()


    def _create(self, event, _supergroup, _creation_mode):
        # Create new object, then call its dialog method with the 'new' flag.
        if _creation_mode is "group":
            c = m.Groups(m.db, "")

            if c._dialog("new", _supergroup._id) is True:
                self._listCtrl.DeleteAllItems()
                _supergroup.load_groups(_supergroup._id, self)

        elif _creation_mode is "event":
            c = m.Events(m.db, "")

            if c._dialog("new") is True:
                self._listCtrl.DeleteAllItems()
                m.e.load_events(self)

        elif _creation_mode is "participants":
            c = p.Participants(m.db, "")

            if c._dialog("new", "", "") is True:
                self._listCtrl.DeleteAllItems()
                self._load_participants_data()

    def _choice_select(self, event, choice_ctrl, other_choice_ctrl):
        # If a group or event was chosen in the registration window's filter, set other drop-down to 'no group/event selected'.
        _selection = choice_ctrl.GetSelection()

        if _selection is not 0:
            other_choice_ctrl.SetSelection(0)

    def _load_participants_data(self):

        # Load either entries of groups registered for the selected event or events the selected group is registered for.
        _group_selection = self._groupSelectionField.GetSelection()
        _event_selection = self._eventSelectionField.GetSelection()

        if _group_selection is not 0 and _event_selection is 0:
            _selection_value = self._groupSelectionField.GetString(_group_selection)
            self._listCtrl.DeleteAllItems()
            p.p.load_participants(self, "group", _selection_value)

        elif _event_selection is not 0 and _group_selection is 0:
            _selection_value = self._eventSelectionField.GetString(_event_selection)
            self._listCtrl.DeleteAllItems()
            p.p.load_participants(self, "event", _selection_value)

    def _menu(self, event):
        # Close current window and return to main menu.
        self.Destroy()
        x = e.Entry()
        x._show()

    def on_close(self, event):
        # Clean termination of the programm on X-icon.
        self.Destroy()
        wx.Exit()
