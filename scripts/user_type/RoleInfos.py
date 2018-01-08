# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import * 

class TRoleInfos(list):
	"""
	"""
	def __init__(self):
		"""
		"""
		list.__init__(self)
		
	def asDict(self):
		data = {
			"dbid"			: self[0],
			"name"			: self[1],
			"career"		: self[2],
			"level"			: self[3],
		}
		
		return data

	def createFromDict(self, dictData):
		self.extend([dictData["dbid"], dictData["name"], dictData["career"], dictData["level"]])
		return self
		
class ROLE_INFOS_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return TRoleInfos().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, TRoleInfos)

role_info_inst = ROLE_INFOS_PICKLER()

class TRoleInfosList(dict):
	"""
	"""
	def __init__(self):
		"""
		"""
		dict.__init__(self)
		
	def asDict(self):
		datas = []
		dct = {"value" : datas}

		for key, val in self.items():
			datas.append(val)
			
		return dct

	def createFromDict(self, dictData):
		for data in dictData["value"]:
			self[data[0]] = data
		return self
		
class ROLE_INFOS_LIST_PICKLER:
	def __init__(self):
		pass

	def createObjFromDict(self, dct):
		return TRoleInfosList().createFromDict(dct)

	def getDictFromObj(self, obj):
		return obj.asDict()

	def isSameType(self, obj):
		return isinstance(obj, TRoleInfosList)

role_info_list_inst = ROLE_INFOS_LIST_PICKLER()