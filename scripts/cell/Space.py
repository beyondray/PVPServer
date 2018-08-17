import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class Space(KBEngine.Entity, ComBehavior):
	"""
	游戏场景，在这里代表野外大地图
	"""
	def __init__(self):
		KBEngine.Entity.__init__(self)
		ComBehavior.__init__(self)
		
		# 一个space代表的是一个抽象的空间，这里向这个抽象的空间添加了几何资源数据，如果数据是3D场景的
		# 该space中使用navigate寻路使用的是3D的API，如果是2D的几何数据navigate使用的是astar寻路
		#resPath = 'spaces/newgame_space_data'
		#KBEngine.addSpaceGeometryMapping(self.spaceID, None, resPath)		
		KBEngine.globalData["space_%i" % self.spaceID] = self.base
		KBEngine.globalData["SpaceID"] = self.spaceID
	
	#--------------------------------------------------------------------------------------------
	#                              Callbacks
	#--------------------------------------------------------------------------------------------
	def onDestroy(self):
		"""
		KBEngine method.
		"""
		ComBehavior.onDestroy(self)
		
		del KBEngine.globalData["space_%i" % self.spaceID]
		self.destroySpace()
		
	def onEnter(self, entityMailbox):
		"""
		defined method.
		进入场景
		"""
		#DEBUG_MSG('Space::onEnter space[%d] entityID = %i.' % (self.spaceUType, entityMailbox.id))
		pass
		
	def onLeave(self, entityID):
		"""
		defined method.
		离开场景
		"""
		#DEBUG_MSG('Space::onLeave space[%d] entityID = %i.' % (self.spaceUType, entityID))
		pass
		

