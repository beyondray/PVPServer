# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from TimerConst import *
from interfaces.ComBehavior import ComBehavior

class MoveObj(KBEngine.Proxy, ComBehavior):
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
		self.sceneAlloc.onMoveObjGetCell(self)
		self.addTimer(1, 0, TIMER_TYPE_CONTROLL)

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		ComBehavior.onTimer(self, tid, userArg)

		if userArg == TIMER_TYPE_CONTROLL:
			self.cell.controllByClient(self.baseRole)


