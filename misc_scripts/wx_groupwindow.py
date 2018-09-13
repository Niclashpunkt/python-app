import wx

class GroupWindow(wx.Frame):
    def __init__(self, parent, title):

        _parent = parent
        _title = title
        # _dummy_data = dummy_data

        wx.Frame.__init__(self, parent, title=_title, size=(500,-1))
        statusBar = self.CreateStatusBar()
        statusBar.PushStatusText("Edit the group's data and then click 'Save'.")

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
        self._submitBtn = wx.Button(self, wx.ID_ANY, "Submit", (_label_margin,_ctrl_offset_list[5]))


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

    def _edit_group(self, _dummy_data):

        self._idField.SetValue(str(_dummy_data[0]))
        self._nameField.SetValue(_dummy_data[1])
        self._leaderField.SetValue(_dummy_data[3])
        self._gradeField.SetSelection(_dummy_data[4] - 1)

        # print(_dummy_data)



dummy_data = (1, 'Rekkared', 1, 'Sigils', 5)

app = wx.App(False)
frame = GroupWindow(None, "Edit Group Data")
frame._edit_group(dummy_data)
app.MainLoop()
