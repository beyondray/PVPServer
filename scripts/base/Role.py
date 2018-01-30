import KBEngine
import time
from Enum import *
from KBEDebug import *
from TimerConst import *
from interfaces.ComBehavior import ComBehavior


class Role(KBEngine.Proxy, ComBehavior):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		ComBehavior.__init__(self)
		self.sceneAlloc = None
		self.accountEntity = None
		self._destroyTimer = 0

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		ComBehavior.onEntitiesEnabled(self)

		KBEngine.globalData["Space"].loginToSpace(self)

	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		ComBehavior.onTimer(self, tid, userArg)

		if userArg == TIMER_TYPE_DESTROY:
			self.destroyCell()		

	def onClientDeath(self):
		"""
		KBEngine method.
		entity丢失了客户端实体
		"""
		ComBehavior.onClientDeath(self)

		# 防止正在请求创建cell的同时客户端断开了， 我们延时一段时间来执行销毁cell直到销毁base
		# 这段时间内客户端短连接登录则会激活entity
		self._destroyTimer = self.addTimer(1, 0, TIMER_TYPE_DESTROY)
		
	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		ComBehavior.onDestroy(self)

		# 销毁SceneAlloc
		if self.sceneAlloc != None:
			self.sceneAlloc.destroy()
			self.sceneAlloc = None	

		# 如果帐号ENTITY存在 则也通知销毁它
		if self.accountEntity != None:
			_time = time.time() - self.accountEntity.relogin
			if _time > 1:
				self.accountEntity.destroy()
				self.accountEntity = None
			else:
				DEBUG_MSG("Role[%i].destroySelf: relogin =%i" % (self.id, _time))

		# 解除引用
		if self.accountEntity != None:
			self.accountEntity.activeRole = None
			self.accountEntity = None

	#--------------------------------------------------------------------------------------------
	#                              req and rec
	#--------------------------------------------------------------------------------------------
	def reqShot(self, masterId, resName, attackType, atk, pos, dir):
		params = {
			"position"	: 	pos,
			"direction"	: 	dir,
			"spaceCell"	: 	KBEngine.globalData["Space"].cell,
			"masterId"	: 	masterId,
			"resName"	:	resName,
			"attackType":	attackType,
			"damage"	: 	atk,
			"bornTime"	:	time.time(),
			"baseRole"	: 	self,
		}

		def spreadShot() :
			for i in range(5): 
				KBEngine.createBaseLocally("Arrow", params)

		def strongShot() :
			KBEngine.createBaseLocally("Arrow", params)

		def shadowShot() :
			KBEngine.createBaseLocally("Arrow", params)		

		result = {
			AttackType.Strong : strongShot,
			AttackType.Frozen : spreadShot,
			AttackType.Shadow : shadowShot,
		}[attackType]()





