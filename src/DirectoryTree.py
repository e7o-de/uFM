# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx
import os

from os.path import expanduser

class DirectoryTree(wx.TreeCtrl):
	def __init__(self, parent, imageProvider):
		super(DirectoryTree, self).__init__(
			parent,
			1,
			wx.DefaultPosition,
			(-1, -1),
			wx.TR_DEFAULT_STYLE | wx.TR_EDIT_LABELS | wx.TR_HIDE_ROOT
		)
		
		root = self.AddRoot('')
		
		self.imageProvider = imageProvider
		self.AssignImageList(imageProvider.imageList)
		self.SetItemImage(root, 3, wx.TreeItemIcon_Normal)
		
		homeDir = expanduser('~')
		# todo: check getlogin, internetz says it's not reliable ;)
		treeHome = self.AppendItem(root, os.getlogin())
		self.SetPyData(treeHome, wx.TreeItemData(homeDir))
		self.SetItemImage(treeHome, self.imageProvider.gfxHome, wx.TreeItemIcon_Normal)
		self.AddDir(treeHome, homeDir)
		
		treeFilesystem = self.AppendItem(root, 'File system')
		self.SetPyData(treeFilesystem, wx.TreeItemData('/'))
		self.SetItemImage(treeFilesystem, self.imageProvider.gfxDisk, wx.TreeItemIcon_Normal)
		self.AddDir(treeFilesystem, '/')
		
		# ToDo: Trash, Network, Desktop ...
		# ToDo: Bookmarks ...
		
		self.Bind(wx.EVT_TREE_ITEM_EXPANDING, self.OnExpandation)
		self.Bind(wx.EVT_TREE_SEL_CHANGED, self.OnSelection)
		
		self.selectionListener = []
	
	def RegisterSelectionListener(self, listener):
		self.selectionListener.append(listener)
	
	def OnSelection(self, event):
		currentPath = self.GetPyData(event.GetItem()).GetData()
		for listener in self.selectionListener:
			listener(currentPath)
	
	def OnExpandation(self, event):
		item = event.GetItem()
		currentPath = self.GetPyData(item).GetData()
		
		(child, cookie) = self.GetFirstChild(item)
		while child.IsOk():
			self.AddDir(child, currentPath + '/' + self.GetItemText(child))
			(child, cookie) = self.GetNextChild(item, cookie)
	
	def AddDir(self, node, path):
		if self.GetChildrenCount(node, False) > 0:
			return
		
		try:
			found = []
			for subdir in os.listdir(path):
				if os.path.isdir(path + '/' + subdir):
					if subdir[:1] != '.':
						# Don't display hidden files;
						# TODO: Option for that ;)
						found.append(subdir)
			
			found.sort()
		except OSError as e:
			# ToDo: No access rights or something
			print "Cannot read %s due to %s" % (path, e.message)
		
		for subdir in found:
			newNode = self.AppendItem(node, subdir)
			self.SetPyData(newNode, wx.TreeItemData(path + '/' + subdir))
			# todo: check if home directory, disc/mount/network etc.
			self.SetItemImage(newNode, self.imageProvider.gfxFolder, wx.TreeItemIcon_Normal)
	
	def SelectPath(self, initPath):
		root = self.GetRootItem()
		(child, cookie) = self.GetFirstChild(root)
		while child.IsOk():
			nodePath = self.GetPyData(child).GetData()
			if nodePath == initPath[0:len(nodePath)]:
				self.SelectItem(child)
				break;
			(child, cookie) = self.GetNextChild(root, cookie)
