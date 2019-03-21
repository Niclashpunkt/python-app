import sqlite3
import wx
import management as m
import participants as p
import entry as e


app = wx.App(False)

x = e.Entry()
x._show()

app.MainLoop()
