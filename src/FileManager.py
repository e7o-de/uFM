# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx

from Consts import Consts
from Tab import Tab
from StandardImages import StandardImages

class FileManager(wx.Frame):
	TITLE = '%s - uFM'
	
	def __init__(self, parent, initialData):
		wx.Frame.__init__(self, parent, size = (850, 400))
		self.SetMinSize((100, 100))
		
		self.initImages(initialData)
		self.initUi()
		self.initMenu()
		
		self.SetTitle(self.TITLE % '(path from tab, todo)')
		
		self.Show(True)
	
	def initImages(self, initialData):
		if initialData != None:
			self.imageProvider = initialData['imageProvider']
		else:
			self.imageProvider = StandardImages(self)
	
	def initUi(self):
		# todo: PyEmbeddedImage for self.SetIcon(...)
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		self.SetSizer(mainSizer)
		self.tabs = wx.Notebook(self, style = wx.NB_TOP)
		self.tabs.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnTabChange)
		mainSizer.Add(self.tabs, 1, wx.EXPAND)
		
		#self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self.OnPageChanged)
		#self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self.OnPageChanging) #event.GetSelection()
		
		self.CreateStatusBar(style = wx.ST_SIZEGRIP)
		self.PushStatusText('Hey, I am the status bar!')
		
		self.OnNewTab(None)
	
	def initMenu(self):
		menu = wx.MenuBar()
		
		# File
		fileMenu = wx.Menu()
		
		m = fileMenu.Append(Consts.ID_NEW_WINDOW, '&New window', 'Opens a new window')
		self.Bind(wx.EVT_MENU, self.OnNewWindow, m)
		
		m = fileMenu.Append(Consts.ID_NEW_TAB, 'New &tab\tCTRL+T', 'Opens a new tab')
		self.Bind(wx.EVT_MENU, self.OnNewTab, m)
		
		fileMenu.AppendSeparator()
		m = fileMenu.Append(Consts.ID_CLOSE_TAB)
		m = fileMenu.Append(Consts.ID_CLOSE_WINDOW, 'Close window', '')
		
		fileMenu.AppendSeparator()
		m = fileMenu.Append(Consts.ID_EXIT)
		
		menu.Append(fileMenu, '&File')
		
		# Edit
		editMenu = wx.Menu()
		m = editMenu.Append(Consts.ID_CUT)
		m = editMenu.Append(Consts.ID_COPY)
		m = editMenu.Append(Consts.ID_PASTE)
		editMenu.AppendSeparator()
		m = editMenu.Append(Consts.ID_SELECT_ALL, 'Select &all\tCTRL+A', 'Selects all files')
		m = editMenu.Append(Consts.ID_SELECT_PATTERN, '&Select pattern\tCTRL+S', 'Select files according to a pattern')
		m = editMenu.Append(Consts.ID_INVERT_SELECTION, '&Invert selection\tCTRL+SHIFT+I', 'Inverts the selection')
		m = editMenu.Append(Consts.ID_SELECT_NONE, 'Select &none\tCTRL+SHIFT+A', 'Removes the current selection')
		editMenu.AppendSeparator()
		m = editMenu.Append(Consts.ID_RENAME, '&Rename\tF2', 'Renames a file')
		
		self.Bind(wx.EVT_MENU, self.ForwardEventToTab, m)
		menu.Append(editMenu, '&Edit')
		
		# View
		viewMenu = wx.Menu()
		menu.Append(viewMenu, '&View')
		
		# Goto
		goMenu = wx.Menu()
		menu.Append(goMenu, '&Go to')
		m = goMenu.Append(Consts.ID_GOTO_LOCATION, '&Location\tCTRL+L', 'Opens a location')
		
		# Tools
		toolsMenu = wx.Menu()
		menu.Append(toolsMenu, '&Tools')
		
		# About
		aboutMenu = wx.Menu()
		m = aboutMenu.Append(Consts.ID_ABOUT, '&About', 'About this program')
		menu.Append(aboutMenu, '&?')
		
		# -- Done
		self.SetMenuBar(menu)
		
		# Keyboard
		self.Bind(wx.EVT_MENU, self.OnMenuRename, id = Consts.ID_RENAME)
		
		#self.accels = wx.AcceleratorTable([
		#	(wx.ACCEL_NORMAL, wx.WXK_F2, Consts.ID_RENAME),
		#])
		#self.SetAcceleratorTable(self.accels)
	
	def OnNewWindow(self, event):
		initialData = {
			'imageProvider': self.imageProvider,
		}
		frame = FileManager(None, initialData)
		frame.Show()
	
	def OnNewTab(self, event):
		tab = Tab(self.tabs, '/', self.imageProvider)
		self.tabs.AddPage(tab, '/', select = True)
		self.activeTab = tab
	
	def OnTabChange(self, event):
		self.activeTab = event.EventObject
	
	def ForwardEventToTab(self, event):
		self.activeTab.OnEvent(event.GetId())
	
	def OnMenuRename(self, event):
		print("Rename")
