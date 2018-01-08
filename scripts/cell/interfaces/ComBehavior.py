# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

#=====================================
# Desc: 服务端游戏对象的公共行为类
#=====================================
class ComBehavior:
	def __init__(self):
		DEBUG_MSG("%s::cell is created: %i" % (self.getClassName(), self.id))

	def getClassName(self):
		return self.__class__.__name__
		
	def controllByClient(self, baseMailbox):
		if baseMailbox != None and baseMailbox.client != None:
			self.controllId = baseMailbox.id
			self.controlledBy = baseMailbox

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getClassName(), self.id, tid, userArg))

	def onWitnessed(self, isWitnessed):
		"""
		KBEngine method.
		此实体是否被观察者(player)观察到, 此接口主要是提供给服务器做一些性能方面的优化工作，
		在通常情况下，一些entity不被任何客户端所观察到的时候， 他们不需要做任何工作， 利用此接口
		可以在适当的时候激活或者停止这个entity的任意行为。
		@param isWitnessed	: 为false时， entity脱离了任何观察者的观察
		"""
		DEBUG_MSG("%s::onWitnessed: %i isWitnessed=%i." % (self.getClassName(), self.id, isWitnessed))

	def onGetWitness(self):
		"""
		KBEngine method.
		绑定了一个观察者(客户端)
		"""
		
		DEBUG_MSG("%s::onGetWitness: %i." % (self.getClassName(), self.id))

	def onLoseWitness(self):
		"""
		KBEngine method.
		解绑定了一个观察者(客户端)
		"""
		DEBUG_MSG("%s::onLoseWitness: %i." % (self.getClassName(), self.id))		

	def onEnterTrap(self, entityEntering, range_xz, range_y, controllerID, userarg):
		"""
		KBEngine method.
		引擎回调进入陷阱触发
		"""
		if entityEntering.getClassName() == "Role":
			DEBUG_MSG("%s::onEnterTrap: %i entityEntering=%i, range_xz=%s, range_y=%s, controllerID=%i, userarg=%i" % \
							(self.getClassName(), self.id, entityEntering.id, range_xz, range_y, controllerID, userarg))

	def onLeaveTrap(self, entityLeaving, range_xz, range_y, controllerID, userarg):
		"""
		KBEngine method.
		引擎回调离开陷阱触发
		"""
		if entityLeaving.getClassName() == "Role":
			DEBUG_MSG("%s::onLeaveTrap: %i entityLeaving=%i, range_xz=%s, range_y=%s, controllerID=%i, userarg=%i" % \
							(self.getClassName(), self.id, entityLeaving.id, range_xz, range_y, controllerID, userarg))

	def onRestore(self):
		"""
		KBEngine method.
		entity的cell部分实体被恢复成功
		"""
		DEBUG_MSG("%s::onRestore: %i, base: %s" % (self.getClassName(), self.id, self.base))

	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		DEBUG_MSG("%s::onDestroy: %i." % (self.getClassName(), self.id))



