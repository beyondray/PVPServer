import KBEngine
import Math
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class Space(KBEngine.Base, ComBehavior):
	"""
	一个可操控cellapp上真正space的实体
	注意：它是一个实体，并不是真正的space，真正的space存在于cellapp的内存中，通过这个实体与之关联并操控space。
	"""
	def __init__(self):
		KBEngine.Base.__init__(self)
		ComBehavior.__init__(self)
		self.createInNewSpace(None)

		self.roles = {}
		
		KBEngine.globalData["Space"] = self

	def spawnCreateMonster(self):
		center = Math.Vector3(101.4286, 0, 18.37545)

		KBEngine.createBaseAnywhere("SpawnPoint", 
					{"spawnEntityNO"	: 2001, 	\
					"position"			: center, 	\
					"direction"			: [0,0,0],		\
					"createToCell"		: self.cell})

	def loginToSpace(self, roleMailbox):
		"""
		defined method.
		某个玩家请求登陆到这个space中
		"""
		roleMailbox.createCell(self.cell)
		self.onEnter(roleMailbox)
		
	def logoutSpace(self, entityID):
		"""
		defined method.
		某个玩家请求登出这个space
		"""
		self.onLeave(entityID)

	def onEnter(self, entityMailbox):
		"""
		defined method.
		进入场景
		"""
		self.roles[entityMailbox.id] = entityMailbox
		
		if self.cell is not None:
			self.cell.onEnter(entityMailbox)
		
	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		if entityID in self.roles:
			del self.roles[entityID]
		
		if self.cell is not None:
			self.cell.onLeave(entityID)

	def onGetCell(self):
		"""
		KBEngine method.
		entity的cell部分实体被创建成功
		"""
		ComBehavior.onGetCell(self)	
		#self.spawnCreateMonster()

	def controllObjByRole(self, objCellMailbox, role_id):
		DEBUG_MSG("%s[%i]::controllObjByRole: %s" % (self.getClassName(), self.id, self.roles[role_id]))
		objCellMailbox.controllByClient(self.roles[role_id])
