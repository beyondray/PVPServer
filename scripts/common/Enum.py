#============================
# desc: 枚举及扩展
#============================

class Enum(tuple): 
	__getattr__ = tuple.index
 

ShotType = Enum(['SHOT_ARC', 'SHOT_AUTO', 'SHOT_SPREAD', 'SHOT_LASER'])

DamgeType = Enum(['Normal', 'Frozen'])

CureType = Enum(['Normal', 'Bless'])
