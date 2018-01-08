import KBEngine
from KBEDebug import *
from Enum import *
from TimerConst import *

class CombatProps:
	def __init__(self):
		pass

	def getClassName(self):
		return self.__class__.__name__

	def reqBeAttack(self, exposed, attackType, damage):
		self.HP -= damage
		if self.HP < 0:
			self.HP = 0

		if attackType == DamgeType.Frozen:
			self.moveSpeed = 3.5
			self.addTimer(3, 0, TIMER_TYPE_FROZEN_RELIEF)

		self.allClients.recAttack(attackType, damage)

		DEBUG_MSG("%s[%i].reqBeAttack: attackType =%f, damage=%f" % (self.getClassName(), self.id, attackType, damage))

	def reqBeCure(self, exposed, cureType, hp):
		self.HP += hp
		if self.HP > self.HP_Max:
			self.HP = self.HP_Max

		self.allClients.recCure(cureType, hp)

		DEBUG_MSG("%s[%i].reqBeCure: cureType =%f, hp=%f" % (self.getClassName(), self.id, cureType, hp))

	def reqRelive(slef, exposed):
		self.HP = self.HP_Max

		DEBUG_MSG("%s[%i].reqRelive: HP =%f" % (self.getClassName(), self.id, self.HP))

	def reqSpeedUp(self, exposed, speed):
		if speed <= self.moveSpeed:
			return

		self.moveSpeed = speed
		self.allClients.recSpeedUp(speed)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		if userArg == TIMER_TYPE_FROZEN_RELIEF:
			self.moveSpeed = 7.0

		DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getClassName(), self.id, tid, userArg))