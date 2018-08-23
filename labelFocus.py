import wx

from re import compile,IGNORECASE

class mainWindow(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,-1,title,size=(500,200),
                        style=wx.DEFAULT_FRAME_STYLE | wx.NO_FULL_REPAINT_ON_RESIZE)

        self.mainPanel=wx.Panel(self,-1)

        # create controls to be subsequently associated with accelerator keys
        self.dateEdit=wx.TextCtrl(self.mainPanel,wx.NewId(),'',(100,20))
        self.comboBox=wx.ComboBox(self.mainPanel,wx.NewId() ,'',(100,40),(-1,-1),[],wx.CB_DROPDOWN)
        self.activityEdit=wx.TextCtrl(self.mainPanel,wx.NewId(),'',(100,60))
        self.hoursEdit=wx.TextCtrl(self.mainPanel,wx.NewId(),'',(100,80))
        self.visitedBox=wx.CheckBox(self.mainPanel,wx.NewId(),'',(100,100))

        # instance a class that accummulates information about controls and accelerators
        accumAcceleratorTable=self.AccumAcceleratorTable(self,self.focusHandler)

        # as each label is created associate appropriate accelerator key with a control
        dateEditLabel=wx.StaticText(self.mainPanel,-1,accumAcceleratorTable ('&Date',self.dateEdit),(10,20))
        clientEditLabel=wx.StaticText(self.mainPanel,-1,accumAcceleratorTable ('&Client',self.comboBox),(10,40))
        activityEditLabel=wx.StaticText(self.mainPanel,-1,accumAcceleratorTable ('&Activity',self.activityEdit),(10,60))
        hoursEditLabel=wx.StaticText(self.mainPanel,-1,accumAcceleratorTable ('&Hours',self.hoursEdit),(10,80))
        visitedEditLabel=wx.StaticText(self.mainPanel,-1,accumAcceleratorTable ('&Visited',self.visitedBox),(10,100))

        # put the accummulated accelerator table and associations to use
        self.SetAcceleratorTable(wx.AcceleratorTable(accumAcceleratorTable.acceleratorTable))
        self.idControlDict=accumAcceleratorTable.idControlDict

        self.Show(True)

    def focusHandler(self,event):
        self.idControlDict[event.GetId()].SetFocus()

    class AccumAcceleratorTable:
        def __init__(self,parent,focusHandler):
            self.acceleratorTable=[]
            self.idControlDict={ }
            self.patt=compile(r'&([a-z])',IGNORECASE)
            self.focusHandler=focusHandler
            self.parent=parent

        def __call__(self,labelText,controlToFocus):
            # find the accelerator key,if any,in the label
            result=self.patt.search(labelText)
            if result:
                anId=wx.NewId()
                self.acceleratorTable.append(( wx.ACCEL_ALT,ord(result.group(1).upper()),anId))
                self.idControlDict[anId]=controlToFocus
                wx.EVT_MENU(self.parent,anId,self.focusHandler)
            return labelText

class App(wx.App):
    def OnInit(self):
        frame=mainWindow(None,-1,"Associating labels with controls")
        self.SetTopWindow(frame)
        return True

if __name__=="__main__":
    app=App(0)
    app.MainLoop()
