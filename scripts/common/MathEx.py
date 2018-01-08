import Math
import math
import random

def calcRandomPos(center, radius):
	r = random.uniform(1.0, radius)
	angle = 360.0 * random.random()
	x = r * math.cos(angle)
	z = r * math.sin(angle) 
	return Math.Vector3(center.x + x, center.y, center.z + z)	