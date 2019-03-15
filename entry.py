import sqlite3
import wx
import management as m

class Entry(object):

    def __init__(self):

        frame = EntryWindow(None, "")

class EntryWindow(wx.Frame):
    def __init__(self, parent, title):

        _title = "Welcome"

        wx.Frame.__init__(self, parent, title=_title, size=(500,200))

        # wred = wx.Window.__init__(self, parent, (-1, -1), (-1, -1))
        # wred = ColWin(self, wx.NewId(), wx.RED)
        self._staticText = wx.StaticText(self, wx.NewId(), "Welcome! Please choose an option to continue.", (-1, -1), wx.DefaultSize, style=wx.ALIGN_CENTRE_HORIZONTAL | wx.ST_NO_AUTORESIZE)
        self._registerBtn = wx.Button(self, wx.NewId(), 'Register &Participants', (-1, -1), wx.DefaultSize)
        self._reportBtn = wx.Button(self, wx.NewId(), 'Generate &Report', (-1, -1), wx.DefaultSize)
        self._eventsBtn = wx.Button(self, wx.NewId(), 'Manage &Events', (-1, -1), wx.DefaultSize)
        self._groupsBtn = wx.Button(self, wx.NewId(), 'Manage &Groups', (-1, -1), wx.DefaultSize)
        # staline = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)

        self._eventsBtn.Bind(wx.EVT_BUTTON,  lambda event: self._manage_events(event))
        self._groupsBtn.Bind(wx.EVT_BUTTON,  lambda event: self._manage_groups(event))
        # self._groupsBtn.Bind(wx.EVT_BUTTON, lambda event, _supergroup=_supergroup: self._edit_selected(event, _groups_list, _supergroup))

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self._registerBtn, 0)
        hsizer1.Add(self._reportBtn, 0, wx.LEFT, b)
        hsizer1.Add(self._eventsBtn, 0, wx.LEFT, b)
        hsizer1.Add(self._groupsBtn, 0, wx.LEFT, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        # vsizer1.Add((20,-1))
        vsizer1.Add(self._staticText, 1,  wx.ALIGN_CENTRE_HORIZONTAL | wx.ALL, 20)
        # vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        self.SetSizer(vsizer1)

        # self.SetAutoLayout(1)
        # vsizer1.Fit(self)

        self.Show()

    def _manage_events(self, event):
        print("manage events called")
        m.e.load_events()
        self.Destroy()

    def _manage_groups(self, event):
        print("manage groups called")
        m.s.load_groups(m.s._id)
        self.Destroy()


app = wx.App(False)
# s = Supergroups(db, 1) #requires database object and the id of the supergroup.
e = Entry()
# As of now, the id is hardcoded, as the app only deals with one supergroup.

app.MainLoop()
