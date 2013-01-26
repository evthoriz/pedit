#!/usr/bin/env python

"""pathEdit.py is designed to present/modify environment variables more friendly"""

import _winreg as winreg
import wx
import string 

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",0,winreg.KEY_ALL_ACCESS)
value,s = winreg.QueryValueEx(key,"Path")
str1 = value.encode('utf8')
str2 = string.replace(str1,';',';\n')


class Frame(wx.Frame):
    def __init__(self,size):
        wx.Frame.__init__(self,parent=None,id=-1,pos=(-1,-1),size=size,title="PathEditor",style=wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU)
        self.panel = wx.Panel(self)
        self.text = wx.TextCtrl(self.panel,-1,pos=(3,3),size=(size[0]-10,size[1]-90),style=wx.HSCROLL|wx.TE_MULTILINE)
        self.text.SetValue(str2)
        self.button1 = wx.Button(self.panel,label="Save",pos=(size[0]-180,size[1]-80))
        self.Bind(wx.EVT_BUTTON,self.OnSaveMe,self.button1)
        self.button2 = wx.Button(self.panel,label="Cancel",pos=(size[0]-90,size[1]-80))
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,self.button2)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Notice: One path a line, end with ';' !")
    def OnSaveMe(self,event):
        newstr1 = self.text.GetValue().encode('utf-8').replace(';\n',';')
        newstr2 = unicode(newstr1)
        winreg.SetValueEx(key,"Path",0,winreg.REG_SZ,newstr2)
        self.statusbar.SetStatusText("Status: Saved already!")
    def OnCloseMe(self,event):
        self.Close(True)
    def OnCloseWindow(self,event):
        self.Destroy()
        
class App(wx.App):
    def OnInit(self):
        self.frame = Frame(size=(480,350))
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


app = App()
app.MainLoop()
