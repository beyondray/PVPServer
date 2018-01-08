# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
from interfaces.ComBehavior import ComBehavior

class SpawnPoint(KBEngine.Base, ComBehavior):
	def __init__(self):
		KBEngine.Base.__init__(self)
		ComBehavior.__init__(self)
		self.createCellEntity(self.createToCell)
		

