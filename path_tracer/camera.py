from .vec3 import Vec3
from .ray import Ray
import math

class Camera:
	def __init__(self, lookFrom, lookAt, vup, vfov, aspect): #vfov is top to bottom in degrees
		theta = (vfov * math.pi) / 180.0
		halfHeight = math.tan(theta / 2.0)
		halfWidth = aspect * halfHeight
		self._origin = lookFrom
		w = Vec3.unitVector(lookFrom - lookAt)
		u = Vec3.unitVector(Vec3.cross(vup, w))
		v = Vec3.cross(w, u)
		self._lowerLeftCorner = self._origin - (halfWidth * u) - (halfHeight * v) - w
		self._horizontal = 2.0 * halfWidth * u
		self._vertical = 2.0 * halfHeight * v

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

	def getRay(self, s, t):
		return Ray(self._origin, self._lowerLeftCorner + (s * self._horizontal) + (t * self._vertical) - self._origin)