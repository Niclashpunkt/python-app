# Name:      LearnSizers1.py
# Purpose:   A demo app to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2005 Jean-Michel Fauth
# Licence:   GPL

# os dev:    windows 98
# py dev:    Python 2.4.1
# wx dev:    wxPython 2.6.1
# Revision:  27 June 2005

# Contributor and minor fixes: Marcelo Barbero, Argentina
# Revision: 03 August 2005

# LearnSizer*.py is a small application aimed to learn the sizers and
# their usage.
# This application is a collection of panels. Each panel contains
# a few widgets laid out with sizers. The panels are numbered
# MyPanel_0 to MyPanel_n. The panel 0 is the simpliest case. The
# order of the panels follows an increasing complexity in the
# layout. It is warmly recommended to start with MyPanel_0.
#
# Do not forget:
# - the wxPython doc
# - the wiki page http://wiki.wxpython.org/index.cgi/UsingSizers
# - dir(<instance of a sizer>) for a list of methods
# - print sizer.method.__doc__
#


import os
import sys
import wx

class ColWin(wx.Window):
    """- A wx.Window with a coloured background
    - pos and size == (-1, -1) since sizers are used"""

    def __init__(self, parent, id, BackColour):
        wx.Window.__init__(self, parent, id, (-1, -1), (-1, -1), wx.SIMPLE_BORDER)
        self.SetBackgroundColour(BackColour)


class MyPanel_0(wx.Panel):
    """- The simpliest sizer, a ColWin
    - use of named arguments"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 20
        vsizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        # or
        # vsizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        vsizer1.Add(item=wgreen, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer1)


class MyPanel_1(wx.Panel):
    """- Two ColWins, vertically"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer1)


class MyPanel_2(wx.Panel):
    """- Three ColWins, horizontally """

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)


class MyPanel_3(wx.Panel):
    """- Three ColWins, horizontally, height ratio 1:2:3"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wblue, 2, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wgreen, 3, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)


class MyPanel_4(wx.Panel):
    """- Two ColWins, vertically, a fixed width of 50 pixels between
    the two items"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add((-1, 50), 0,  wx.ALL, b)
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer1)


class MyPanel_5(wx.Panel):
    """- Two items: a ColWin and a Button, vertically
    - the Button is either left/right aligned or centered
    - comment / uncomment for testing the Button alignment
    - wx.ALIGN_LEFT is the default value"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        b1 = wx.Button(self, wx.NewId(), 'button1', (-1, -1), wx.DefaultSize)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        #~ vsizer1.Add(b1, 0, wx.ALIGN_LEFT | wx.ALL, b)
        #~ vsizer1.Add(b1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.Add(b1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        self.SetSizer(vsizer1)


class MyPanel_6(wx.Panel):
    """- Three items: a ColWin and two Buttons
    - the Buttons are either left/right aligned or centered"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        b1 = wx.Button(self, wx.NewId(), '&OK', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), '&Cancel', (-1, -1), wx.DefaultSize)

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        #~ vsizer1.Add(hsizer1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        #~ vsizer1.Add(hsizer1, 0, wx.ALIGN_LEFT | wx.ALL, b)
        self.SetSizer(vsizer1)


class MyPanel_7(wx.Panel):
    """- Four items: a ColWin, two Buttons, and a StaticLine
    - the Buttons are either left/right aligned or centered
    - the height of the static line == 2, the wx.GROW flag specifies an
      horizontal expansion, since the StaticLine is in a vertical sizer"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        b1 = wx.Button(self, wx.NewId(), '&OK', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), '&Cancel', (-1, -1), wx.DefaultSize)
        staline = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        self.SetSizer(vsizer1)


class MyPanel_8(wx.Panel):
    """- 7 items: 2 ColWins and 5 Buttons
    - ColWins: one is sizable, the other not
    - Buttons at the right of the frame
    - something like a toolbar at the right"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wwhite = ColWin(self, wx.NewId(), wx.WHITE)

        b1 = wx.Button(self, wx.NewId(), '1', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), '2', (-1, -1), wx.DefaultSize)
        b3 = wx.Button(self, wx.NewId(), '3', (-1, -1), wx.DefaultSize)
        b4 = wx.Button(self, wx.NewId(), '4', (-1, -1), wx.DefaultSize)
        b5 = wx.Button(self, wx.NewId(), '5', (-1, -1), wx.DefaultSize)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 3
        vsizer1.Add(wred, 1, wx.EXPAND | wx.BOTTOM, b)
        vsizer1.Add(wwhite, 0, wx.EXPAND, b)

        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        vsizer2.Add(b1, 0, wx.BOTTOM, b)
        vsizer2.Add(b2, 0, wx.BOTTOM, b)
        vsizer2.Add(b3, 0, wx.BOTTOM, b)
        vsizer2.Add(b4, 0, wx.BOTTOM, b)
        vsizer2.Add(b5, 0, wx.BOTTOM, b)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 10
        hsizer1.Add(vsizer1, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM, b)
        hsizer1.Add(vsizer2, 0, wx.EXPAND| wx.ALL, b)

        self.SetSizer(hsizer1)


class MyPanel_9(wx.Panel):
    """- 7 items: 2 ColWins and 5 Buttons
    - the ColWins are sizable
    - the Buttons have a fixed height and a default width
    - something like a toolbar at the top"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wwhite = ColWin(self, wx.NewId(), wx.WHITE)

        h = 40
        b1 = wx.Button(self, wx.NewId(), '1', (-1, -1), (-1, h))
        b2 = wx.Button(self, wx.NewId(), '2', (-1, -1), (-1, h))
        b3 = wx.Button(self, wx.NewId(), '3', (-1, -1), (-1, h))
        b4 = wx.Button(self, wx.NewId(), '4', (-1, -1), (-1, h))
        b5 = wx.Button(self, wx.NewId(), '5', (-1, -1), (-1, h))

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0)
        hsizer1.Add(b3, 0)
        hsizer1.Add(b4, 0)
        hsizer1.Add(b5, 0)

        b = 2
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(wred, 1, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wwhite, 1, wx.EXPAND | wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND, b)
        vsizer1.Add(hsizer2, 1, wx.ALL | wx.EXPAND, b)

        self.SetSizer(vsizer1)


class MyPanel_10(wx.Panel):
    """- Three ColWins in a StaticBoxSizer, vertically"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 10  #inside the staticbox
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'StaticboxSizer with a caption'), wx.VERTICAL)
        vsbsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsbsizer1)


class MyPanel_11(wx.Panel):
    """- Three ColWins in a StaticBoxSizer, vertically
    - the StaticBoxSizer is in a sizer to enable a border"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 10  #inside the staticbox
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'StaticboxSizer with a caption'), wx.VERTICAL)
        vsbsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)

        b = 20
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(vsbsizer1, 1, wx.EXPAND | wx.ALL, b)

        self.SetSizer(hsizer1)


class MyPanel_12(wx.Panel):
    """- 5 ColWins, vertically
    - ColWins 2 and 4 are in StaticBoxSizer"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)
        wwhite = ColWin(self, wx.NewId(), wx.WHITE)
        wyellow = ColWin(self, wx.NewId(), wx.NamedColour('yellow'))

        b = 10
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'blue'), wx.VERTICAL)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)

        vsbsizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'white'), wx.VERTICAL)
        vsbsizer2.Add(wwhite, 1, wx.EXPAND | wx.ALL, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(vsbsizer1, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(vsbsizer2, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wyellow, 1, wx.EXPAND | wx.ALL, b)

        self.SetSizer(vsizer1)


class MyPanel_13(wx.Panel):
    """- 3 StaticBoxSizers with a ColWin in each
    - the StaticBoxSizers are arranged vertically"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.NamedColour('red'))
        wgreen = ColWin(self, wx.NewId(), wx.NamedColour('green'))
        wblue = ColWin(self, wx.NewId(), wx.NamedColour('blue'))

        b = 10
        sizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'Staticbox'), wx.VERTICAL)
        sizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        sizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'Staticbox'), wx.VERTICAL)
        sizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)

        sizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.NewId(), 'Staticbox'), wx.VERTICAL)
        sizer4.Add(wblue, 1, wx.EXPAND | wx.ALL, b)

        #tricky: the 2nd and 3rd staticbox sizer are shifted one pixel to the
        #left, try with b2 = 0
        b1, b2 = 0, -1
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer3.Add(sizer1, 1, wx.EXPAND, b1)
        sizer3.Add(sizer2, 1, wx.EXPAND | wx.LEFT, b2)
        sizer3.Add(sizer4, 1, wx.EXPAND | wx.LEFT, b2)

        self.SetSizer(sizer3)


class MyPanel_14(wx.Panel):
    """- 3 ColWins, horizontally, 2 spacers with a fixed height"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, wx.NewId(), wx.RED)
        wblue = ColWin(self, wx.NewId(), wx.BLUE)
        wgreen = ColWin(self, wx.NewId(), wx.GREEN)

        b = 0
        h = 20
        hsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add((-1, h))
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add((-1, h))
        hsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)


class MyPanel_15(wx.Panel):
    """- 4 items: a ColWin and 3 Buttons
    - Buttons 1 and 3 are left/right aligned, Button 2 is centered
    - use of spacers to set a gap between the Buttons.
    - better way?"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wgreen = ColWin(self, wx.NewId(), wx.NamedColour('green'))
        b1 = wx.Button(self, wx.NewId(), 'button1', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), 'button2', (-1, -1), wx.DefaultSize)
        b3 = wx.Button(self, wx.NewId(), 'button3', (-1, -1), wx.DefaultSize)

        b = 0
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b2, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b3, 0, wx.ALL, b)

        #tip: this does not work
        #~ b = 0
        #~ hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        #~ hsizer1.Add(b1, 0, wx.ALIGN_LEFT, b)
        #~ hsizer1.Add(b2, 0, wx.ALIGN_CENTER, b)
        #~ hsizer1.Add(b3, 0, wx.ALIGN_RIGHT, b)

        b = 5
        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        vsizer2.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer2)


class MyPanel_16(wx.Panel):
    """- 4 items: a ColWin, 3 Buttons
    - Buttons 1 and 3 are top/bottom aligned, Button 2 is centered
    - use of spacers to set a gap between the Buttons
    - better way?"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wgreen = ColWin(self, wx.NewId(), wx.NamedColour('green'))
        b1 = wx.Button(self, wx.NewId(), 'button1', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), 'button2', (-1, -1), wx.DefaultSize)
        b3 = wx.Button(self, wx.NewId(), 'button3', (-1, -1), wx.DefaultSize)

        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b1, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b2, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b3, 0, wx.ALL, b)

        b = 5
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(vsizer1, 0, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer2)


class MyPanel_17(wx.Panel):
    """- An input box"""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        s = 'abc' + os.linesep + 'def' + os.linesep + 'ghi'
        statxt = wx.StaticText(self, -1, s, (-1, -1), (-1, -1))
        txt = wx.TextCtrl(self, wx.NewId(), 'input', (-1, -1), (-1, -1))
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, -1), wx.LI_HORIZONTAL)

        b1 = wx.Button(self, wx.NewId(), "&OK", (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), "&Cancel", (-1, -1), wx.DefaultSize)

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(txt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.SetMinSize((300, -1))
        self.SetSizerAndFit(vsizer1)

        #the items are not sizable, once set, pass the fitted size to
        #the parent
        self.parent.SetClientSize(vsizer1.GetSize())


class MyPanel_18(wx.Panel):
    """- A message box"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        s = 'This is a rather long message with.'
        s += (os.linesep + 'a lot of lines...')*20

        statxt = wx.StaticText(self, -1, s, (-1, -1), (-1, -1))
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, -1), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.NewId(), "&OK", (-1, -1), wx.DefaultSize)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(b1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        vsizer1.SetMinSize((200, -1))
        self.SetSizerAndFit(vsizer1)

        self.parent.SetClientSize(vsizer1.GetSize())


class MyPanel_19(wx.Panel):
    """- A serie of couples, StaticText-TextCtrl
    - Buttons ok and cancel"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        lab1 = wx.StaticText(self, -1, 'hydrogen :', (-1, -1), (-1, -1), wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, -1, 'tin :', (-1, -1), (-1, -1), wx.ALIGN_RIGHT)
        lab3 = wx.StaticText(self, -1, 'mendelevium :', (-1, -1), (-1, -1), wx.ALIGN_RIGHT)
        lab4 = wx.StaticText(self, -1, 'carbon :', (-1, -1), (-1, -1), wx.ALIGN_RIGHT)
        txt1 = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        txt2 = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        txt3 = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        txt4 = wx.TextCtrl(self, -1, '', (-1, -1), (-1, -1))
        b1 = wx.Button(self, wx.NewId(), '&OK', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, wx.NewId(), '&Cancel', (-1, -1), wx.DefaultSize)
        staline = wx.StaticLine(self, wx.NewId(), (-1, -1), (-1, 2), wx.LI_HORIZONTAL)

        b = 5
        w = 100
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(lab1, 0, wx.RIGHT, b)
        hsizer1.Add(txt1, 1, wx.GROW, b)
        hsizer1.SetItemMinSize(lab1, (w, -1))

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(lab2, 0, wx.RIGHT, b)
        hsizer2.Add(txt2, 1, wx.GROW, b)
        hsizer2.SetItemMinSize(lab2, (w, -1))

        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add(lab3, 0, wx.RIGHT, b)
        hsizer3.Add(txt3, 1, wx.GROW, b)
        hsizer3.SetItemMinSize(lab3, (w, -1))

        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(lab4, 0, wx.RIGHT, b)
        hsizer4.Add(txt4, 1, wx.GROW, b)
        hsizer4.SetItemMinSize(lab4, (w, -1))

        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(b1, 0)
        hsizer5.Add(b2, 0, wx.LEFT, 10)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer4, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer5, 0, wx.ALIGN_RIGHT | wx.ALL, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())


class MyPanel_20(wx.Panel):
    """- A FlexGridSizer
    - 4 ColWins as cells, all sizeable"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wred = ColWin(self, -1, wx.RED)
        wblue = ColWin(self, -1, wx.BLUE)
        wwhite = ColWin(self, -1, wx.WHITE)
        wcyan = ColWin(self, -1, wx.CYAN)

        hgap, vgap = 0, 0
        nrows, ncols = 2, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)

        b = 5
        fgs.AddMany([(wred, 1, wx.EXPAND | wx.ALL, b),
                     (wblue, 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan, 1, wx.EXPAND | wx.ALL, b),
                    ])

        # or
        #~ fgs.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wwhite, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wcyan, 1, wx.EXPAND | wx.ALL, b)

        #set all rows and cols sizable, try to comment / uncomment
        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(1)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)

        self.SetSizer(fgs)


class MyPanel_21(wx.Panel):
    """- A FlexgridSizer with 4 cells
    - cell (0, 0) is a column of 3 Buttons
    - cell (1, 1) is a row of 3 Buttons
    - cell (1, 0) is empty
    - cell (0, 1) is a ColWin"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wwhite = ColWin(self, -1, wx.WHITE)
        b1 = wx.Button(self, -1, 'button1', (-1, -1), wx.DefaultSize)
        b2 = wx.Button(self, -1, 'button2', (-1, -1), wx.DefaultSize)
        b3 = wx.Button(self, -1, 'button3', (-1, -1), wx.DefaultSize)
        b4 = wx.Button(self, -1, 'button4', (-1, -1), wx.DefaultSize)
        b5 = wx.Button(self, -1, 'button5', (-1, -1), wx.DefaultSize)
        b6 = wx.Button(self, -1, 'button6', (-1, -1), wx.DefaultSize)

        b = 0
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b2, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b3, 0, wx.ALL, b)

        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b4, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b5, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b6, 0, wx.ALL, b)

        hgap, vgap = 0, 0
        nrows, ncols = 2, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)

        b = 5
        fgs.AddMany([(vsizer1, 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (hsizer1, 1, wx.EXPAND | wx.ALL, b),
                    ])

        #really tricky ;-)
        fgs.AddGrowableRow(0)
        fgs.AddGrowableCol(1)

        self.SetSizer(fgs)


class MyPanel_22(wx.Panel):
    """- A FlexGridSizer of 9 cells (3x3) with 5 ColWins in cells
    and 4 empty cells"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        wwhite = ColWin(self, -1, wx.WHITE)
        wblue = ColWin(self, -1, wx.BLUE)
        wgreen = ColWin(self, -1, wx.GREEN)
        wcyan = ColWin(self, -1, wx.CYAN)
        wred = ColWin(self, -1, wx.RED)

        hgap, vgap = 0, 0
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)

        b = 5
        fgs.AddMany([(wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wblue, 1, wx.EXPAND | wx.ALL, b),

                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wgreen, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),

                     (wred, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wcyan, 1, wx.EXPAND | wx.ALL, b),
                    ])

        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(1)
        fgs.AddGrowableRow(2)

        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)

        self.SetSizer(fgs)


class MyPanel_23(wx.Panel):
    """- A FlexGridSizer of 9 cells (3x3) with 4 ColWins in cells and 5 empty cells
    - rows 1 and 3 have a fixed size"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)

        h = 40
        wwhite = wx.Window(self, -1, (-1, -1), (-1, h), wx.SIMPLE_BORDER)
        wwhite.SetBackgroundColour(wx.WHITE)
        wblue = ColWin(self, -1, wx.BLUE)
        wgreen = ColWin(self, -1, wx.GREEN)
        wred = wx.Window(self, -1, (-1, -1), (-1, h), wx.SIMPLE_BORDER)
        wred.SetBackgroundColour(wx.RED)

        hgap, vgap = 0, 0
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)

        b = 5
        fgs.AddMany([((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),

                     (wblue, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wgreen, 1, wx.EXPAND | wx.ALL, b),

                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wred, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                    ])

        fgs.AddGrowableRow(1)

        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)

        self.SetSizer(fgs)


class MyPanel_24(wx.Panel):
    """- This example is coming from one of my applications
    - in the real app, the white window is a drawing area and
      the five lower windows are StaticTexts with a defined
      font size (this is why I force a fixed height)"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        #a menu for the beauty of the demo
        menu1 = wx.Menu()
        menu1.Append(101, '&aaa')
        menuBar = wx.MenuBar()
        menuBar.Append(menu1, '&File')
        self.parent.SetMenuBar(menuBar)

        wwhite = ColWin(self, -1, wx.WHITE)
        wblue = ColWin(self, -1, wx.BLUE)
        wgreen = ColWin(self, -1, wx.GREEN)
        wcyan = ColWin(self, -1, wx.CYAN)
        wred = ColWin(self, -1, wx.RED)
        wcoral = ColWin(self, -1, wx.NamedColour('coral'))
        staline = wx.StaticLine(self, -1, (-1, -1), (-1, 2), wx.LI_HORIZONTAL)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.BOTTOM, b)
        vsizer1.Add(wgreen, 1, wx.EXPAND)

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        minhe = 100
        hsizer2.Add(wcoral, 2, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wcyan, 3, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wred, 3, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(vsizer1, 2, wx.EXPAND, border=b)
        hsizer2.SetItemMinSize(wcoral, (-1, minhe))
        hsizer2.SetItemMinSize(wcyan, (-1, minhe))
        hsizer2.SetItemMinSize(wred, (-1, minhe))
        hsizer2.SetItemMinSize(vsizer1, (-1, minhe))

        vsizer3 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        vsizer3.Add(staline, 0, wx.GROW | wx.ALL, 0)
        vsizer3.Add(wwhite, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, b)
        vsizer3.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)

        self.SetSizerAndFit(vsizer3)


class MyPanel_25(wx.Panel):
    """- This shows the relaton between the font size and the size of the
      widgets when sizers are used"""

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        fs = 20
        self.SetFont(wx.Font(fs, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))


        statxt1 = wx.StaticText(self, -1, 'one, two, three', (-1, -1), (-1, -1))
        statxt1.SetBackgroundColour(wx.WHITE)
        statxt2 = wx.StaticText(self, -1, 'eins, zwei, drei', (-1, -1), (-1, -1))
        statxt3 = wx.StaticText(self, -1, 'un, deux, trois', (-1, -1), (-1, -1))
        b1 = wx.Button(self, wx.NewId(), 'button1', (-1, -1), (-1, -1))
        b2 = wx.Button(self, wx.NewId(), 'button2', (-1, -1), (-1, -1))

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(b2, 1, wx.EXPAND | wx.ALL, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt1, 0, wx.ALL, b)
        vsizer1.Add(statxt2, 0, wx.ALL, b)
        vsizer1.Add(statxt3, 0, wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALL, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())


class TestComboBox(wx.Panel):
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id)

        sampleList = []
        for i in range(0, 26):
            sampleList.append('MyPanel_' + str(i))

        st = wx.StaticText(self, -1, "Select the example you want to see."
                         "Then click the View button.", (-1, -1))

        doctxt = wx.StaticText(self, -1, "")
        doctxt.SetLabel(MyPanel_0.__doc__)
        self.doctxt = doctxt

        # This combobox is created with a preset list of values.
        cb = wx.ComboBox(
            self, -1, "MyPanel_0", (-1, -1),
            (-1, -1), sampleList, wx.CB_DROPDOWN
            )
        self.cb = cb

        stline = wx.StaticLine(self, -1, (-1, -1), (-1, 2), wx.LI_HORIZONTAL)

        btnView = wx.Button(self, -1, "&View")
        self.Bind(wx.EVT_BUTTON, self.OnClickView, btnView)

        btnExit = wx.Button(self, -1, "E&xit")
        self.Bind(wx.EVT_BUTTON, self.OnClickExit, btnExit)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(st, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(cb, 0, wx.EXPAND | wx.ALL, 0)
        vsizer1.Add(doctxt, 0, wx.EXPAND | wx.ALL, b)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(btnView, 0)
        hsizer1.Add(btnExit, 0, wx.LEFT, b)

        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(vsizer1, 5, wx.EXPAND | wx.ALL, 0)
        vsizer2.Add(stline, 0, wx.GROW | wx.ALL, b)
        vsizer2.Add(hsizer1, 1, wx.ALIGN_RIGHT | wx.ALL, b)
        self.SetSizer(vsizer2)

        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, cb)

    # When the user selects something, we go here.
    def EvtComboBox(self, evt):
        self.doctxt.SetLabel(eval('%s.__doc__' % self.cb.GetValue()))

    def OnClickView(self, evt):
        win = wx.Frame(self, -1, self.cb.GetValue(), size=(350, 200),
                  style = wx.DEFAULT_FRAME_STYLE)
        eval('%s(win)' % self.cb.GetValue())

        win.CenterOnScreen()
        win.Show(True)

    def OnClickExit(self, evt):
        sys.exit()



class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        s = __file__
        wx.Frame.__init__(self, parent, id, s, (0, 0), (500, 400))

        self.panel = eval('MyPanel_%d(self)' % panel)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.Destroy()


class MyApp(wx.App):

    def OnInit(self):
        frame = wx.Frame(None, -1, __file__, (0, 0), (400, 300))
        frame.panel = TestComboBox(frame, -1)
        frame.Show(True)
        self.SetTopWindow(frame)
        return True


def main():
    app = MyApp(False)
    app.MainLoop()


if __name__ == "__main__" :
    main()
