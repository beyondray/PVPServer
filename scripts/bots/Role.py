import KBEngine
from KBEDebug import *
import Math
import MathEx

from interfaces.GameObject import GameObject
from interfaces.Motion import Motion
from interfaces.Combat import Combat


class Role(KBEngine.Entity, 
			GameObject,
			Motion,
			Combat):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		GameObject.__init__(self)
		Motion.__init__(self)
		Combat.__init__(self)

	def recvDamage(self, attackerID, skillID, damageType, damage):
		"""
		defined.
		"""
		DEBUG_MSG("%s::recvDamage: %i attackerID=%i, skillID=%i, damageType=%i, damage=%i" % \
			(self.getScriptName(), self.id, attackerID, skillID, damageType, damage))

	def onEnterSpace(self):
		"""
		KBEngine method.l
		这个entity进入了一个新的space
		"""
		DEBUG_MSG("%s::onEnterSpace: %i" % (self.__class__.__name__, self.id))

	def onLeaveSpace(self):
		"""
		KBEngine method.
		这个entity将要离开当前space
		"""
		DEBUG_MSG("%s::onLeaveSpace: %i" % (self.__class__.__name__, self.id))
		
	def onBecomePlayer( self ):
		"""
		KBEngine method.
		当这个entity被引擎定义为角色时被调用
		"""
		DEBUG_MSG("%s::onBecomePlayer: %i" % (self.__class__.__name__, self.id))


	def update(self):
		pass

class PlayerRole(Role):
	def __init__(self):
		self.randomWalkRadius = 10.0
		self.spawnPosition = Math.Vector3( self.position )
		#self.spawnPosition.y = 0.0
		self.walkToDest = True

	def onEnterSpace(self):
		"""
		KBEngine method.
		这个entity进入了一个新的space
		"""
		DEBUG_MSG("%s::onEnterSpace: %i" % ("Bot", self.id))
		pass

	def onLeaveSpace(self):
		"""
		KBEngine method.
		这个entity将要离开当前space
		"""
		DEBUG_MSG("%s::onLeaveSpace: %i" % ("Bot", self.id))
		pass
		
	def onBecomePlayer( self ):
		"""
		KBEngine method.
		当这个entity被引擎定义为角色时被调用
		"""
		DEBUG_MSG("%s::onBecomePlayer: %i" % ("Bot", self.id))

		self.__init__()
		KBEngine.callback(1, self.update)

	def gotoPosition(self, position, dist = 0.0):
		"""
		virtual method.
		移动到位置
		"""

		if self.position.distTo(position) <= 0.05:
			return

		speed = self.moveSpeed 
		

		if dist > 0.0:
			destPos = Math.Vector3(position) - self.position
			destPos.normalise()
			destPos *= dist
			destPos = position - destPos
		else:
			destPos = Math.Vector3(position)
		
		self.moveToPoint(destPos, speed, 0, None, 1, 1)

	def update(self):
		if self.isDestroyed:
			return

		#self.position  = self.calcRandomWalkPosition()
		DEBUG_MSG("Bot:update: called!!")
		dest = MathEx.calcRandomPos(self.spawnPosition, self.randomWalkRadius)
		self.moveSpeed = 80
		self.gotoPosition( dest)
		# dest = Math.Vector3(0, 0, 0)
		# if self.walkToDest :
		# 	dest = self.calcRandomWalkPosition()
		# 	self.walkToDest = False

		# _dir = dest - self.position
		# length = math.sqrt(_dir.x * _dir.x + _dir.y * _dir.y + _dir.z * _dir.z)
		# _dir = Math.Vector3(_dir.x / length, _dir.y / length, _dir.z /length)
		# self.position.x += _dir.x * 3.0
		# self.position.y += _dir.y * 3.0
		# self.position.z += _dir.z * 3.0
		# if self.position.z - dest.z < 0.1 :
		# 	self.walkToDest = True

	def onMoveOver(self, controllerId, userarg):
		"""
		KBEngine method.
		使用引擎的任何移动相关接口， 在entity移动结束时均会调用此接口
		"""
		KBEngine.callback(10, self.update)
		            
