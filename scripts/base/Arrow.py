# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class Arrow(KBEngine.Proxy, ComBehavior):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		ComBehavior.__init__(self)
		self.createCell(self.spaceCell)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------					
	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		ComBehavior.onGetCell(self)

		self.cell.controllByClient(self.baseRole)


