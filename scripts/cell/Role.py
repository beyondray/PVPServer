import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior
from interfaces.CombatProps import CombatProps
from interfaces.AniState import AniState

class Role(KBEngine.Entity, 
		ComBehavior,
		CombatProps,
		AniState):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		ComBehavior.__init__(self)
		CombatProps.__init__(self)
		AniState.__init__(self)

	def reqActiveArrows(self, exposed, timestamp):
		self.otherClients.recShot(0, timestamp)

		DEBUG_MSG("%s[%i].reqActiveArrows: timestamp =%f" % (self.getClassName(), self.id, timestamp))

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onTimer(self, tid, userArg):
		"""
		KBEngine method.
		引擎回调timer触发
		"""
		CombatProps.onTimer(self, tid, userArg)

		DEBUG_MSG("%s::onTimer: %i, tid:%i, arg:%i" % (self.getClassName(), self.id, tid, userArg))



