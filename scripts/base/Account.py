# -*- coding: utf-8 -*-
import KBEngine
import time
import Math, MathEx
from KBEDebug import *
from GlobeConst import *
from RoleInfos import TRoleInfos

class Account(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		self.relogin = time.time()
		self.activeRole = None
		
	def onEntitiesEnabled(self):
		"""
		KBEngine method.
		该entity被正式激活为可使用， 此时entity已经建立了client对应实体， 可以在此创建它的
		cell部分。
		"""
		INFO_MSG("account[%i] entities enable. mailbox:%s" % (self.id, self.client))
			
	def onLogOnAttempt(self, ip, port, password):
		"""
		KBEngine method.
		客户端登陆失败时会回调到这里
		"""
		INFO_MSG(ip, port, password)

		# 如果一个在线的账号被一个客户端登陆并且onLogOnAttempt返回允许
		# 那么会踢掉之前的客户端连接
		# 那么此时self.activeRole可能不为None， 常规的流程是销毁这个角色等新客户端上来重新选择角色进入
		if self.activeRole:
			self.activeRole.giveClientTo(self)
			self.relogin = time.time()
			self.activeRole.destroyCell()
			self.activeRole = None
			
		return KBEngine.LOG_ON_ACCEPT

	def onClientDeath(self):
		"""
		KBEngine method.
		客户端对应实体已经销毁
		"""
		if self.activeRole:
			self.activeRole.accountEntity = None
			self.activeRole = None

		DEBUG_MSG("Account[%i].onClientDeath:" % self.id)
		self.destroy()		
		
	def onDestroy(self):
		"""
		KBEngine method.
		entity销毁
		"""
		DEBUG_MSG("Account::onDestroy: %i." % self.id)
		
		if self.activeRole:
			self.activeRole.accountEntity = None

			try:
				self.activeRole.destroySelf()
			except:
				pass
				
			self.activeRole = None		

	def reqRoleList(self):
		if self.client :
			self.client.recRoleList(0, self.characters)	

	def reqCreateRole(self, name, career):
		self.params = {
			"name" : name,
			"career" : career,
			"level" : 1,
		}
		KBEngine.executeRawDatabaseCommand("select * from tbl_Role where sm_name='%s'" % name, self.sqlcallback)

	def sqlcallback(self, result, rows, insertid, error):
		#success
		if len(result) == 0:
			role = KBEngine.createBaseLocally("Role", self.params)
			role.cellData["position"] = MathEx.calcRandomPos(Relive_Center, Relive_Radius)
			if role :
				role.writeToDB(self._onDatabaseSaved)
		#fail
		else:
			self.params["dbid"] = 0
			info = TRoleInfos().createFromDict(self.params)		
			if self.client :
				self.client.recCreateRole(1, info)

	def _onDatabaseSaved(self, success, role):
		if success :
			params = {
				"dbid" : role.databaseID,
				"name" : role.cellData["name"],
				"career": role.cellData["career"],
				"level" : 1
			}
			#self.characters["value"].extend([params])
			info = TRoleInfos().createFromDict(params)
			self.characters[role.databaseID] = info
			self.writeToDB()

			role.destroy()
			if self.client :
				self.client.recCreateRole(0, info)

	def reqRemoveRole(self, dbid):
		_dbid = 0
		if dbid in self.characters :
			KBEngine.deleteBaseByDBID("Role", dbid, self._onRoleDataRemove, "default")
			del self.characters[dbid]
			_dbid = dbid

		if self.client :
			self.client.recRemoveRole(_dbid)

	def _onRoleDataRemove(self, success):
		if not success :
			ERROR_MSG("Account[%i]::_onRoleDataRemove: the role data is using!" % (self.id))
		else :
			DEBUG_MSG("Account[%i]::_onRoleDataRemove: remove the role data success!" % (self.id))		


	def reqEnterGame(self, dbid):
		if self.activeRole is None:
			if dbid in self.characters:
				self.lastSelCharacter = dbid
				# 由于需要从数据库加载角色，因此是一个异步过程，加载成功或者失败会调用__onRoleCreated接口
				# 当角色创建好之后，account会调用giveClientTo将客户端控制权（可理解为网络连接与某个实体的绑定）切换到Role身上，
				# 之后客户端各种输入输出都通过服务器上这个Role来代理，任何proxy实体获得控制权都会调用onEntitiesEnabled
				# Role继承了Teleport，Teleport.onEntitiesEnabled会将玩家创建在具体的场景中
				KBEngine.createBaseFromDBID("Role", dbid, self.__onRoleCreated)
			else:
				ERROR_MSG("Account[%i]::selectRoleGame: not found dbid(%i)" % (self.id, dbid))
		else:
			self.giveClientTo(self.activeRole)

	def __onRoleCreated(self, baseRef, dbid, wasActive):
		"""
		选择角色进入游戏时被调用
		"""
		if wasActive:
			ERROR_MSG("Account::__onRoleCreated:(%i): this character is in world now!" % (self.id))
			return
		if baseRef is None:
			ERROR_MSG("Account::__onRoleCreated:(%i): the character you wanted to created is not exist!" % (self.id))
			return
			
		role = KBEngine.entities.get(baseRef.id)
		if role is None:
			ERROR_MSG("Account::__onRoleCreated:(%i): when character was created, it died as well!" % (self.id))
			return
		
		if self.isDestroyed:
			ERROR_MSG("Account::__onRoleCreated:(%i): i dead, will the destroy of Role!" % (self.id))
			role.destroy()
			return
				
		role.accountEntity = self
		self.activeRole = role 

		sceneAlloc = self.createSceneAlloc()
		self.giveClientTo(sceneAlloc)
		#self.giveClientTo(role)

	def createSceneAlloc(self):
		sceneAlloc = KBEngine.createBaseLocally( "SceneAlloc", {} )
		sceneAlloc.role = self.activeRole
		self.activeRole.sceneAlloc = sceneAlloc
		return sceneAlloc
