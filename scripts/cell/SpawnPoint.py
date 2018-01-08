# -*- coding: utf-8 -*-
import KBEngine
from TimerConst import *
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

import d_entities

class SpawnPoint(KBEngine.Entity, ComBehavior):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		ComBehavior.__init__(self)
		self.addTimer(1, 0, SCDefine.TIMER_TYPE_SPAWN)
		
	def spawnTimer(self):
		datas = d_entities.datas.get(self.spawnEntityNO)
		
		if datas is None:
			ERROR_MSG("SpawnPoint::spawn:%i not found." % self.spawnEntityNO)
			return
			
		params = {
			"spawnID"	: self.id,
			"spawnPos" : tuple(self.position),
			"uid" : datas["id"],
			"utype" : datas["etype"],
			"modelID" : datas["modelID"],
			"modelScale" : self.modelScale,
			"dialogID" : datas["dialogID"],
			"name" : datas["name"],
			"descr" : datas.get("descr", ''),
		}
		
		e = KBEngine.createEntity(datas["entityType"], self.spaceID, tuple(self.position), tuple(self.direction), params)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		ComBehavior.onTimer(self)
		if  userArg == TIMER_TYPE_SPAWN:
			self.spawnTimer()

	def onRestore(self):
		"""
		KBEngine method.
		entity的cell部分实体被恢复成功
		"""
		ComBehavior.onRestore(self)
		self.addTimer(1, 0, TIMER_TYPE_SPAWN)
	
	def onEntityDestroyed(self, entityNO):
		"""
		defined.
		出生的entity销毁了 需要重建?
		"""
		self.addTimer(1, 0, TIMER_TYPE_SPAWN)
		
