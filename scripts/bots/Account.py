# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Account(KBEngine.Entity):
	user_id = 0

	def __init__(self):
		KBEngine.Entity.__init__(self)
		Account.user_id += 1
		self.user_id = Account.user_id
		self.base.reqRoleList()

	def recRoleList(self, res, infos):
		if res == 0 :
			if len(infos['value']) > 0 :
				self.base.reqEnterGame(infos['value'][0]["dbid"])
			else :
				name = "玩家_%s" % self.user_id
				self.base.reqCreateRole(name, 1)

		DEBUG_MSG("Account:recRoleList::%s, res=%i" % (list(infos['value']), res))

	def recCreateRole(self, res, info):
		if res == 0 :
			dbid = info["dbid"]
			self.base.reqEnterGame(dbid)

		DEBUG_MSG("Account:recCreateRole:: dbid=%i, res=%i" % (dbid, res))

	def recRemoveRole(self, dbid):
		pass


