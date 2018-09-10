import sqlite3

import wx

class Supergroups(object):

    def __init__(self, db, id):
        self._db = db
        self._id = id
        self.load_groups(self._id)
        # print("init supergroups")


    def load_groups(self, _id):

        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        groups_list = []
        for g in groups_data:
            # print(g)
            groups_list.append(Groups(self._db, g))
        # print(groups_list)

        frame = GroupListWindow(None, "hello")
        frame._display_groups(groups_data, groups_list, self)

    def refresh_groups(self, _id, _frame):

        cursor_groups = self._db.cursor()
        cursor_groups.execute('''SELECT * FROM groups WHERE super_group_id = ?;''', (str(self._id)))
        groups_data = cursor_groups.fetchall()

        groups_list = []
        for g in groups_data:
            # print(g)
            groups_list.append(Groups(self._db, g))

        _frame._display_groups(groups_data, groups_list, self)

        # group0 = groups_list[0]

    #     return groups_list
    #
    #
    #     # group0._edit()
    # def _edit_group(self, group):
    #     groups_list = load_groups()
    #     print("groups_list loaded")

class Groups(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list
        # print(self._list[1])

    def _edit(self):

        # print(self._list)

        # app = wx.App(False)
        dlg = GroupWindow(None, "", "edit")
        dlg._edit_group(self._list, self)

        if dlg.ShowModal() == wx.ID_OK:

            if dlg._gradeField.GetSelection()+1 is 0:
                _grade = dlg._gradeField.GetValue()
            else:
                _grade = dlg._gradeField.GetSelection()+1

            _new_data = (
                int(dlg._idField.GetValue()),
                dlg._nameField.GetValue(),
                self._list[2],
                dlg._leaderField.GetValue(),
                _grade)

            self._update(self._list, _new_data)
            return True

        dlg.Destroy()
        # app.MainLoop()

    def _update(self, _list, _new_data):

        if _list != _new_data:
            # print("update")
            cursor_update = self._db.cursor()
            print(_new_data)
            cursor_update.execute('''UPDATE groups SET name = ?, leader = ?, grade = ? WHERE id = ? ''',
            (_new_data[1], _new_data[3], _new_data[4], _list[0]))

            self._db.commit()





class GroupWindow(wx.Dialog):
    def __init__(self, parent, title, dialog_mode):

        _parent = parent
        _dialog_mode = dialog_mode

        if _dialog_mode is "edit":
            _title = "Edit Group Data"
            _status_text = "Edit the group's data and then click 'Save'."

        # _dummy_data = dummy_data

        wx.Dialog.__init__(self, parent, title=_title, size=(500,-1))
        # statusBar = self.CreateStatusBar()
        # statusBar.PushStatusText(_status_text)

        _label_margin = 5
        _ctrl_margin = 75
        _ctrl_offset_list = []
        _label_offset_list = []
        for row in range(0,6):
            _ctrl_offset = 20 + 20*row + 3*row
            _label_offset = _ctrl_offset + 3
            _ctrl_offset_list.append(_ctrl_offset)
            _label_offset_list.append(_label_offset)

        # print(_label_offset_list)

        self._idLabel = wx.StaticText(self, wx.ID_ANY, 'Group ID',    (_label_margin,_label_offset_list[0]))
        self._nameLabel = wx.StaticText(self, wx.ID_ANY, 'Name',  (_label_margin,_label_offset_list[1]))
        self._leaderLabel = wx.StaticText(self, wx.ID_ANY, 'Leader',  (_label_margin,_label_offset_list[2]))
        self._gradeLabel = wx.StaticText(self, wx.ID_ANY, 'Grade',  (_label_margin,_label_offset_list[3]))



        self._idField = wx.TextCtrl(self,wx.ID_ANY, "2",    (_ctrl_margin,_ctrl_offset_list[0]), (20,20), style=wx.TE_READONLY)
        self._nameField = wx.TextCtrl(self,wx.ID_ANY, "",   (_ctrl_margin,_ctrl_offset_list[1]))
        self._leaderField = wx.TextCtrl(self,wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[2]))
        self._gradeField = wx.ComboBox(self, wx.ID_ANY, "", (_ctrl_margin,_ctrl_offset_list[3]), choices=['1','2','3','4','5','6','Other'], style=0)
        self._gradeField.SetSelection(0)
        self._submitBtn = wx.Button(self, wx.ID_OK, "Save", (_label_margin,_ctrl_offset_list[5]))
        self._exitBtn = wx.Button(self, wx.ID_CANCEL , "Cancel", (_ctrl_margin + _label_margin*6,_ctrl_offset_list[5]))

        # self._submitBtn.Bind(wx.EVT_BUTTON, self._save)
        # self._exitBtn.Bind(wx.EVT_BUTTON, self._exit)

        # Use some sizers to see layout options
        # self._sizer = wx.BoxSizer(wx.VERTICAL)
        # self._sizer.Add(self._idLabel, 0, wx.EXPAND)
        # self._sizer.Add(self._idField, 0, wx.EXPAND)
        # self._sizer.Add(self._nameField, 0, wx.EXPAND)
        #
        # self.SetSizer(self._sizer)
        # self.SetAutoLayout(1)
        # self._sizer.Fit(self)


    def _edit_group(self, _data, _g):

        self.dialog_mode = "edit"

        self._idField.SetValue(str(_data[0]))
        self._nameField.SetValue(_data[1])
        self._leaderField.SetValue(_data[3])
        self._gradeField.SetSelection(_data[4] - 1)

class GroupListWindow(wx.Frame):
    def __init__(self, parent, title):

        # _groups_list = groups_list
        # _supergroup = supergroup
        _parent = parent
        _title = "Groups in Supergroup XY"

        wx.Frame.__init__(self, parent, title=_title, size=(500,300))

        panel = wx.Panel(self, -1)

        _margin = 5

        self._listLabel = wx.StaticText(panel, wx.ID_ANY, 'Groups', (_margin,_margin))

        self._listCtrl = wx.ListCtrl(panel, wx.ID_ANY, (_margin,25), style=wx.LC_REPORT)
        self._listCtrl.AppendColumn("ID", format=wx.LIST_FORMAT_LEFT, width=50)
        self._listCtrl.AppendColumn("Name", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
        self._listCtrl.AppendColumn("Leader", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
        self._listCtrl.AppendColumn("Grade", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)
        self._listCtrl.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=wx.LIST_AUTOSIZE)

        self._editBtn = wx.Button(panel, wx.ID_ANY, "Edit Selected", (_margin, 200))
        self._createBtn = wx.Button(panel, wx.ID_ANY, "Create New Group", (_margin+100, 200))

        # self._editBtn.Bind(wx.EVT_BUTTON, self._edit_selected(self, _groups_list))
        # self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list, _supergroup=_supergroup: self._edit_selected(event, _groups_list, _supergroup))
        # self._createBtn.Bind(wx.EVT_BUTTON, self._create)



    def _display_groups(self, _groups_data, _groups_list, _supergroup):

        # groups_list = _groups_list

        self._editBtn.Bind(wx.EVT_BUTTON, lambda event, _groups_list=_groups_list, _supergroup=_supergroup: self._edit_selected(event, _groups_list, _supergroup))
        self._createBtn.Bind(wx.EVT_BUTTON, self._create)

        for g in _groups_data:

            _index = self._listCtrl.InsertItem(0, str(g[0]))
            # print(g[0])
            self._listCtrl.SetItem(_index, 1, str(g[1]))
            self._listCtrl.SetItem(_index, 2, str(g[3]))
            self._listCtrl.SetItem(_index, 3, str(g[4]))
            # self._listCtrl.SetItem(_index, 3, )

        self.Show()

    def _edit_selected(self, event, _groups_list, _supergroup):
        # print(_groups_list)
        _selection = self._listCtrl.GetFirstSelected()


        print(_supergroup)

        # print(int(_selected_id))
        if _selection > -1 and _selection <= self._listCtrl.GetColumnCount():
        # if 1 == 1:
            # print("edit!")
            _selected_id = self._listCtrl.GetItemText(_selection)
            group_to_edit = _groups_list[int(_selected_id)-1]
            if group_to_edit._edit() is True:
                self._listCtrl.DeleteAllItems()
                _supergroup.refresh_groups(_supergroup._id, self)
            # _groups_list[_selection]._edit()

    def _create(self, event):
        print("New")


# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')


app = wx.App(False)
s = Supergroups(db, 1) #requires database object and the id of the supergroup
# dummy_data = (1, 'Rekkared', 1, 'Sigils', 5)
app.MainLoop()
