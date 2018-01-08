import KBEngine
from TimerConst import *
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class Arrow(KBEngine.Entity, ComBehavior):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		ComBehavior.__init__(self)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------	
	def onTimer(self, tid, userArg):
		ComBehavior.onTimer(self, tid, userArg)
		if userArg == TIMER_TYPE_DESTROY:
			self.kill = True
			self.destroy()
			DEBUG_MSG("%s::destroy: %i" % (self.getClassName(), self.id))
			return

	#--------------------------------------------------------------------------------------------
	#                              req and rec
	#--------------------------------------------------------------------------------------------
	def reqDestroySelf(self, exposed):
		#因为子弹销毁时可能有数据传输，所以延迟一段时间销毁
		self.addTimer(0.2, 0, TIMER_TYPE_DESTROY)

		DEBUG_MSG("%s::reqDestroySelf: %i" % (self.getClassName(), self.id))


