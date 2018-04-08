from .vec3 import Vec3
from .ray import Ray

class Camera:
	def __init__(self):
		self._lowerLeftCorner = Vec3(-2.0, -1.0, -1.0)
		self._horizontal = Vec3(4.0, 0.0, 0.0)
		self._vertical = Vec3(0.0, 2.0, 0.0)
		self._origin = Vec3(0.0, 0.0, 0.0)

	@property
	def LowerLeftCorner(self):
		return self._lowerLeftCorner

	@property
	def Horizontal(self):
		return self._horizontal

	@property
	def Vertical(self):
		return self._vertical

	@property
	def Origin(self):
		return self._origin

	def getRay(self, u, v):
		return Ray(self._origin, self._lowerLeftCorner + (v * self._vertical) + (u * self._horizontal) - self._origin)