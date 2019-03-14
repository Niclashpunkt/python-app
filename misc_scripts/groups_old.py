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
            print(g)
            groups_list.append(Groups(self._db, g))
        print(groups_list)

        group0 = groups_list[0]
        # print("g0:")
        # print(group0._list)
        group0._edit()

        # return groups_data


class Groups(object):

    def __init__(self, db, list):
        self._db = db
        self._list = list
        # print(self._list[1])

    def _edit(self):

        print(self._list)

        app = wx.App(False)
        frame = GroupWindow(None, "", "edit")
        frame._edit_group(self._list, self)
        app.MainLoop()

    def _update(self, _list, _new_data):

        print("updated!")


class GroupWindow(wx.Frame):
    def __init__(self, parent, title, dialog_mode):

        _parent = parent
        _dialog_mode = dialog_mode

        if _dialog_mode is "edit":
            _title = "Edit Group Data"
            _status_text = "Edit the group's data and then click 'Save'."

        # _dummy_data = dummy_data

        wx.Frame.__init__(self, parent, title=_title, size=(500,-1))
        statusBar = self.CreateStatusBar()
        statusBar.PushStatusText(_status_text)

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
        self._submitBtn = wx.Button(self, wx.ID_ANY, "Save", (_label_margin,_ctrl_offset_list[5]))
        self._exitBtn = wx.Button(self, wx.ID_ANY, "Cancel", (_ctrl_margin + _label_margin*6,_ctrl_offset_list[5]))

        self._submitBtn.Bind(wx.EVT_BUTTON, self._save)
        self._exitBtn.Bind(wx.EVT_BUTTON, self._exit)

        # Use some sizers to see layout options
        # self._sizer = wx.BoxSizer(wx.VERTICAL)
        # self._sizer.Add(self._idLabel, 0, wx.EXPAND)
        # self._sizer.Add(self._idField, 0, wx.EXPAND)
        # self._sizer.Add(self._nameField, 0, wx.EXPAND)
        #
        # self.SetSizer(self._sizer)
        # self.SetAutoLayout(1)
        # self._sizer.Fit(self)
        self.Show()

    def _edit_group(self, _data, _g):

        self.dialog_mode = "edit"

        self._idField.SetValue(str(_data[0]))
        self._nameField.SetValue(_data[1])
        self._leaderField.SetValue(_data[3])
        self._gradeField.SetSelection(_data[4] - 1)
        # print(_dummy_data)

    def _save(self, event):

        _new_data = (
            int(self._idField.GetValue()),
            self._nameField.GetValue(),
            "",
            self._leaderField.GetValue(),
            self._gradeField.GetSelection()+1)
        print(_new_data)
        
        # print(_dialog_mode)


        # g.update()

    def _exit(self, event):
        print("abort")

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('data/mydb.db')



s = Supergroups(db, 1) #requires database object and the id of the supergroup
# dummy_data = (1, 'Rekkared', 1, 'Sigils', 5)
