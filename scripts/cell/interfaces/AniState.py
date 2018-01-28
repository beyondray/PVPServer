import KBEngine
from KBEDebug import *

class AniState:
	def __init__(self):
		pass

	def getClassName(self):
		return self.__class__.__name__
		
	def reqSyncAniState(self, exposed, aniInfoDic):
		if self.die != aniInfoDic["die"]:
			self.die = aniInfoDic["die"]

		if self.run != aniInfoDic["run"]:
			self.run = aniInfoDic["run"]

		if self.atk != aniInfoDic["atk"]:
			self.atk = aniInfoDic["atk"]

		DEBUG_MSG("%s[%i]::reqSyncAniState: %s" % (self.getClassName(), self.id, aniInfoDic))