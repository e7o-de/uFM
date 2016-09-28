#! /usr/bin/python

import wx
from FileManager import FileManager

app = wx.App(False)
frame = FileManager(None, None)
frame.Show()
app.MainLoop()
