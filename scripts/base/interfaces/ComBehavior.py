# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

#=====================================
# Desc: 服务端游戏对象的公共行为类
#=====================================
class ComBehavior:
	def __init__(self):
		pass

	def getClassName(self):
		return self.__class__.__name__

	def createCell(self, space):
		"""
		defined method.
		创建cell实体
		"""
		if self.cell is None:
			self.createCellEntity(space)

	def destroyCell(self):
		if self.client is not None:
			return
			
		if self.cell is not None:
			# 销毁cell实体
			self.destroyCellEntity()
			return

	def destroySelf(self):					
		# 销毁base
		if not self.isDestroyed:
			self.destroy()

	#--------------------------------------------------------------------------------------------
	#                              Base Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		DEBUG_MSG("%s[%i]::onTimer: tid:%i, arg:%i." % (self.getClassName(), self.id, tid, userArg))

	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		DEBUG_MSG("%s[%i]::onDestroy." % (self.getClassName(), self.id))

	#--------------------------------------------------------------------------------------------
	#                              Cell Callbacks
	#--------------------------------------------------------------------------------------------	
	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		DEBUG_MSG("%s[%i]::onGetCell: %s." % (self.getClassName(), self.id, self.cell))
		
	def onLoseCell(self):
		"""
		KBEngine method.
		entity的cell部分实体丢失
		"""
		self.destroySelf()
		DEBUG_MSG("%s[%i]::onLoseCell." % (self.getClassName(), self.id))

	def onRestore(self):
		"""
		KBEngine method.
		entity的cell部分实体被恢复成功
		"""
		DEBUG_MSG("%s[%i]::onRestore: %s." % (self.getClassName(), self.id, self.cell))

	#--------------------------------------------------------------------------------------------
	#                              Client Callbacks
	#--------------------------------------------------------------------------------------------	
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		DEBUG_MSG("%s[%i]::onEntitiesEnabled: %s." % (self.getClassName(), self.id, self.client))

	def onClientDeath(self):
		"""
		KBEngine method.
		entity丢失了客户端实体
		"""
		DEBUG_MSG("%s[%i]::onClientDeath." % (self.getClassName(), self.id))
			
	def onClientGetCell(self):
		"""
		KBEngine method.
		客户端已经获得了cell部分实体的相关数据
		"""
		DEBUG_MSG("%s[%i]::onClientGetCell: %s." % (self.getClassName(), self.id, self.client))