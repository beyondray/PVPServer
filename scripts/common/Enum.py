#============================
# desc: 枚举及扩展
#============================

class Enum(tuple): 
	__getattr__ = tuple.index
 

AttackType = Enum(['Normal', 'Frozen', 'Strong'])

CureType = Enum(['Normal', 'Bless'])

ReliefType = Enum(['Frozen', 'SpeedUp', 'Sleep'])
