from .vec3 import Vec3

class HitRecord:
	def __init__(self, t, p, normal, material):
		self._t = t
		self._p = p
		self._normal = normal 
		self._material = material

	@property
	def T(self):
		return self._t 

	@property
	def P(self):
		return self._p 

	@property
	def Normal(self):
		return self._normal

	@property
	def Material(self):
		return self._material

class Hitable:
	def __init__(self, material):
		self._material = material

	@property
	def Material(self):
		return self._material

	def hit(self, r, tmin, tmax):
		#Hit, HitRecord
		return (False, None)