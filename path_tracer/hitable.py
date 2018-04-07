from .vec3 import Vec3

class HitRecord:
	def __init__(self, t = 0.0, p = Vec3(), normal = Vec3()):
		self._t = t
		self._p = p
		self._normal = normal 

	@property
	def T(self):
		return self._t 

	@property
	def P(self):
		return self._p 

	@property
	def Normal(self):
		return self._normal


class Hitable:
	def hit(self, r, tmin, tmax):
		return (False, HitRecord())