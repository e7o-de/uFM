# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx

class StandardImages:
	def __init__(self, parent):
		self.imageList = wx.ImageList(16, 16)
		
		self.gfxFolder = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_FOLDER, wx.ART_OTHER, (16, 16)))
		self.gfxDisk = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_HARDDISK, wx.ART_OTHER, (16, 16)))
		self.gfxRemovable = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_REMOVABLE, wx.ART_OTHER, (16, 16)))
		self.gfxCd = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_CDROM, wx.ART_OTHER, (16, 16)))
		self.gfxHome = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_HOME, wx.ART_OTHER, (16, 16)))
		self.gfxFile = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_NORMAL_FILE, wx.ART_OTHER, (16, 16)))
		self.gfxExecutable = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_EXECUTABLE_FILE, wx.ART_OTHER, (16, 16)))
		
		self.gfxListView = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_LIST_VIEW, wx.ART_OTHER, (16, 16)))
		self.gfxReportView = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_OTHER, (16, 16)))
		
		self.gfxDirUp = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_DIR_UP, wx.ART_OTHER, (16, 16)))
		self.gfxGoBack = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_OTHER, (16, 16)))
		self.gfxGoForward = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_OTHER, (16, 16)))
		self.gfxGoUp = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_UP, wx.ART_OTHER, (16, 16)))
		self.gfxGoDown = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN, wx.ART_OTHER, (16, 16)))
		
		self.gfxCut = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_OTHER, (16, 16)))
		self.gfxCopy = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_OTHER, (16, 16)))
		self.gfxPaste = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_OTHER, (16, 16)))
		self.gfxPrint = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_PRINT, wx.ART_OTHER, (16, 16)))
		self.gfxNew = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_NEW, wx.ART_OTHER, (16, 16)))
		self.gfxNewDir = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_NEW_DIR, wx.ART_OTHER, (16, 16)))
		self.gfxDelete = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_OTHER, (16, 16)))
		self.gfxFind = self.imageList.Add(wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_OTHER, (16, 16)))

