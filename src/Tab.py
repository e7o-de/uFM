# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx

from DirectoryTree import DirectoryTree
from FileView import FileView

class Tab(wx.Panel):
	TITLE = '%s - uFM'
	
	def __init__(self, parent, initPath, imageProvider):
		wx.Panel.__init__(self, parent, size = (850, 400))
		
		self.currentPath = initPath
		self.InitControls(imageProvider)
		self.tree.SelectPath(initPath)
	
	def InitControls(self, imageProvider):
		# Window with splitter and panes
		self.splitter = wx.SplitterWindow(self, -1, style = wx.SP_LIVE_UPDATE)
		self.splitter.SetMinimumPaneSize(25)
		# Workaround for wx bug in gtk when window parent is not sized yet
		wx.CallAfter(self.splitter.SetSashPosition, 200)
		
		leftPanel = wx.Panel(self.splitter, -1)
		leftBox = wx.BoxSizer(wx.VERTICAL)
		leftPanel.SetSizer(leftBox)
		
		rightPanel = wx.Panel(self.splitter, -1)
		rightBox = wx.BoxSizer(wx.VERTICAL)
		rightPanel.SetSizer(rightBox)
		
		# Left treeview
		self.tree = DirectoryTree(leftPanel, imageProvider)
		leftBox.Add(self.tree, 1, wx.EXPAND)
		
		# Right fileview
		self.file = FileView(rightPanel, imageProvider)
		rightBox.Add(self.file, 1, wx.EXPAND)
		
		# Connect everything ;)
		self.tree.RegisterSelectionListener(self.file.ShowPath)
		# ToDo: From file to tree
		# ToDo: Tab title/window title
		
		# Init
		self.splitter.SplitVertically(leftPanel, rightPanel)
		
		sizer = wx.BoxSizer(wx.VERTICAL)
		sizer.Add(self.splitter, 1, wx.EXPAND)
		self.SetSizer(sizer)
	
	def OnEvent(self, eventId):
		print(str(eventId))
