import KBEngine
import MathEx
from KBEDebug import *
from Enum import *
from TimerConst import *
from GlobeConst import *

class CombatProps:
	def __init__(self):
		self.recover_timer = self.addTimer(1, Delta_Time, TIMER_TYPE_RECOVER_3P)
		self.speed_Timer = 0
		pass

	def getClassName(self):
		return self.__class__.__name__

	def addValue(self, curV, deltaV, maxV):
		curV += deltaV
		if curV > maxV:
			curV = maxV
		return curV

	def cutValue(self, curV, deltaV, minV):
		curV -= deltaV
		if curV < minV:
			curV = minV
		return curV

	def reqBeAttack(self, exposed, attackType, damage):
		self.HP = self.cutValue(self.HP, damage, 0.0)
		#if self.HP == 0.0 : self.delTimer(self.recover_timer)

		if attackType == AttackType.Frozen:
			self.moveSpeed = Frozen_Speed
			if self.speed_Timer > 0:
				self.delTimer(self.speed_Timer)
				self.speed_Timer = 0
			self.addTimer(Frozen_Time, 0, TIMER_TYPE_FROZEN_RELIEF)
		elif attackType == AttackType.Strong:
			self.addTimer(Sleep_Time, 0, TIMER_TYPE_SLEEP_RELIEF)

		self.allClients.recAttack(attackType, damage)

		DEBUG_MSG("%s[%i].reqBeAttack: attackType =%f, damage=%f" % (self.getClassName(), self.id, attackType, damage))

	def reqBeCure(self, exposed, cureType, hp):
		self.HP = self.addValue(self.HP, hp, self.HP_Max)

		self.allClients.recCure(cureType, hp)

		DEBUG_MSG("%s[%i].reqBeCure: cureType =%f, hp=%f" % (self.getClassName(), self.id, cureType, hp))

	def reqUseMP(self, exposed, mp):
		self.MP = self.cutValue(self.MP, mp, 0)

	def reqRelive(self, exposed):
		self.addTimer(Relive_Time, 0, TIMER_TYPE_START_RELIVE)

		self.allClients.recRelive(MathEx.calcRandomPos(Relive_Center, Relive_Radius))

		DEBUG_MSG("%s[%i].reqRelive: HP =%f" % (self.getClassName(), self.id, self.HP))

	def reqSpeedUp(self, exposed, speed, needPP):
		self.moveSpeed = speed
		self.PP = self.cutValue(self.PP, needPP, 0)
		self.speed_Timer = self.addTimer(SpeedUp_Time, 0, TIMER_TYPE_SPEEDUP_RELIEF)
		self.allClients.recSpeedUp(speed)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		if userArg == TIMER_TYPE_RECOVER_3P:
			if self.HP > 0.0:
				self.HP = self.addValue(self.HP, Delta_Time * HP_Recover_Speed, self.HP_Max)
				self.MP = self.addValue(self.MP, Delta_Time * MP_Recover_Speed, self.MP_Max)
				self.PP = self.addValue(self.PP, Delta_Time * PP_Recover_Speed, self.PP_Max)
			return

		elif userArg == TIMER_TYPE_FROZEN_RELIEF:
			self.moveSpeed = Normal_Speed
			self.allClients.recRelief(ReliefType.Frozen)

		elif userArg == TIMER_TYPE_SPEEDUP_RELIEF:
			self.moveSpeed = Normal_Speed
			self.allClients.recRelief(ReliefType.SpeedUp)

		elif userArg == TIMER_TYPE_SLEEP_RELIEF:
			self.allClients.recRelief(ReliefType.Sleep)

		elif userArg == TIMER_TYPE_START_RELIVE:
			self.position = MathEx.calcRandomPos(Relive_Center, Relive_Radius)
			self.HP = self.HP_Max
			self.MP = self.MP_Max
			self.PP = self.PP_Max


		DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getClassName(), self.id, tid, userArg))