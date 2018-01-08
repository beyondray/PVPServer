import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class MoveObj(KBEngine.Entity, ComBehavior):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		ComBehavior.__init__(self)

	def reqControll(self, exposed, roleId):
		KBEngine.globalData["Space"].controllObjByRole(self, roleId)


