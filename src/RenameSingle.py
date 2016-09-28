# uFM (c) 2016 Sven Herzky
# Licensed under the terms of the GNU General Public License, version 3 of the
# License, or (at your option) any later version. See LICENSE file.

import wx

class RenameSingle(wx.Dialog):
	def __init__(self, *args, **kw):
		super(RenameSingle, self).__init__(*args, **kw)
		self.SetSize((350, 100))
		self.SetTitle('Rename file')
	
	def x(self):
		print "test"
