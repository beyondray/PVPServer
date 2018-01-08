import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class SceneAlloc(KBEngine.Proxy, ComBehavior):
	_moveObjs = {}

	def __init__(self):
		KBEngine.Proxy.__init__(self)
		ComBehavior.__init__(self)

		#KBEngine.globalData['SceneAlloc'] = self
		#self.createCellEntity(self.spaceCell)

	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onMoveObjGetCell(self, baseMailbox):
		pass

	def onDestroy(self):
		ComBehavior.onDestroy(self)

		# for k, v in _moveObjs.items() :
		# 	v.destroyCellEntity()
		# _moveObjs.clear()

	#--------------------------------------------------------------------------------------------
	#                              req and rec
	#--------------------------------------------------------------------------------------------
	def reqMoveObjSync(self, name, pos, dir):
		DEBUG_MSG("%s[%i]::reqMoveObjSync: %s %s %s" % (self.getClassName(), self.id, name, pos, dir))

		if name in SceneAlloc._moveObjs.keys() :
			self.giveClientTo(self.role)
			return

		params = {
			"name"			: name,
			"position"		: pos, 	
			"direction"		: dir,		
			"spaceCell" 	: KBEngine.globalData["Space"].cell,
			"sceneAlloc"	: self,
			"baseRole"		: self.role,
		}
		moveObj = KBEngine.createBaseLocally("MoveObj", params)
		SceneAlloc._moveObjs[name] = moveObj
		self.giveClientTo(self.role)

	def reqMoveObjsSync(self, moveobjInfoslist):
		DEBUG_MSG("%s[%i]::reqMoveObjsSync: %s" % (self.getClassName(), self.id, moveobjInfoslist))

		for mjInfo in moveobjInfoslist:
			name = mjInfo["name"]
			if name not in SceneAlloc._moveObjs.keys():
				params = {
					"name"			: name,
					"position"		: mjInfo["pos"], 	
					"direction"		: mjInfo["dir"],		
					"spaceCell" 	: KBEngine.globalData["Space"].cell,
					"sceneAlloc"	: self,
					"baseRole"		: self.role,
				}
				moveObj = KBEngine.createBaseLocally("MoveObj", params)
				SceneAlloc._moveObjs[name] = moveObj

		self.giveClientTo(self.role)




