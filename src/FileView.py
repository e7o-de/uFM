# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx
import os

#import sys #tmp

class FileView(wx.ListCtrl):
	def __init__(self, parent, imageProvider):
		super(FileView, self).__init__(
			parent,
			1,
			wx.DefaultPosition,
			(-1, -1),
			wx.LC_REPORT
		)
		
		self.InsertColumn(0, 'Name')
		self.SetColumnWidth(0, 200)
		self.InsertColumn(1, 'Size', wx.LIST_FORMAT_RIGHT)
		self.InsertColumn(2, 'UID')
		self.InsertColumn(3, 'GID')
		self.InsertColumn(4, 'Modified')
		self.InsertColumn(5, 'Created')
		self.InsertColumn(6, 'Inode', wx.LIST_FORMAT_RIGHT)
		self.InsertColumn(7, 'Mode')
		
		self.imageProvider = imageProvider
		self.AssignImageList(imageProvider.imageList, which = wx.IMAGE_LIST_SMALL)
		self.displayedFiles = {}
		
		self.Bind(wx.wx.EVT_LIST_ITEM_ACTIVATED, self.OnDoubleClick, self)
	
	def OnDoubleClick(self, event):
		# todo: multiple selection
		selected = self.displayedFiles[self.GetItemData(event.m_itemIndex)]
		if self.currentPath == '/':
			fullPath = '/' + selected
		else:
			fullPath = self.currentPath + '/' + selected
		
		if os.path.isdir(fullPath):
			self.ShowPath(fullPath)
			# todo: notify treeview, parent ...
		else:
			print('TODO: Opening ' + fullPath)
	
	def OnRename(self, event):
		# Single rename (todo: multiple, see dbl click)
		rename = ChangeDepthDialog(self)
		rename.ShowModal()
		rename.Destroy()
	
	def ShowPath(self, path):
		self.currentPath = path
		
		try:
			# TODO: Check wx.ColumnSorterMixin
			foundDirs = []
			foundFiles = []
			for filename in os.listdir(path):
				if filename[:1] != '.':
					# Don't display hidden files;
					# TODO: Option for that and do some SetItemBackgroundColor stuff or so
					if os.path.isdir(path + '/' + filename):
						foundDirs.append(filename)
					else:
						foundFiles.append(filename)
			
			# TODO: Use this magic sorter mixin thingy
			# import wx.lib.mixins.listctrl as listmix
			foldersOnTop = True
			if foldersOnTop:
				foundDirs.sort()
				foundFiles.sort()
				found = foundDirs + foundFiles
			else:
				found = foundDirs + foundFiles
				found.sort()
		
		except OSError as e:
			print "Cannot read %s due to %s" % (path, e.message)
		
		self.Freeze()
		self.DeleteAllItems()
		idx = 0
		self.displayedFiles = {}
		for filename in found:
			try:
				filedata = os.stat(path + '/' + filename)
			except OSError as e:
				# todo: happens e.g. on broken symlinks
				print 'TODO Error reading file info for %s' % filename
			
			newNode = self.InsertStringItem(idx, filename)
			self.SetStringItem(idx, 1, self.FormatSize(filedata.st_size))
			self.SetStringItem(idx, 2, str(filedata.st_uid))
			self.SetStringItem(idx, 3, str(filedata.st_gid))
			self.SetStringItem(idx, 4, str(filedata.st_mtime))
			self.SetStringItem(idx, 5, str(filedata.st_ctime))
			self.SetStringItem(idx, 6, str(filedata.st_ino))
			
			accessRights = str(oct(filedata.st_mode & 0777))
			self.SetStringItem(idx, 7, accessRights) # todo: https://docs.python.org/2/library/stat.html
			
			self.displayedFiles[idx] = filename
			self.SetItemData(idx, idx) #TODO, required?
			
			# todo: more icon choices ;)
			# todo: check is done already above
			if os.path.isdir(path + '/' + filename):
				self.SetItemImage(newNode, self.imageProvider.gfxFolder, wx.TreeItemIcon_Normal)
			else:
				self.SetItemImage(newNode, self.imageProvider.gfxFile, wx.TreeItemIcon_Normal)
			
			idx += 1
		self.Thaw()
	
	def FormatSize(self, filesize):
		for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
			if abs(filesize) < 1024.0:
				return "%3.1f %s%s" % (filesize, unit, 'B')
			filesize /= 1024.0
		return "%.1f%s%s" % (filesize, 'Yi', suffix)
