from .vec3 import Vec3
from .ray import Ray
import math
from random import random

class Camera:
	def __init__(self, lookFrom, lookAt, vup, vfov, aspect, aperature, focusDist): #vfov is top to bottom in degrees
		self._lensRadius = aperature / 2.0
		theta = (vfov * math.pi) / 180.0
		halfHeight = math.tan(theta / 2.0)
		halfWidth = aspect * halfHeight
		self._origin = lookFrom
		self._w = Vec3.unitVector(lookFrom - lookAt)
		self._u = Vec3.unitVector(Vec3.cross(vup, self._w))
		self._v = Vec3.cross(self._w, self._u)
		self._lowerLeftCorner = self._origin - (halfWidth * focusDist * self._u) - (halfHeight * focusDist * self._v) - (focusDist * self._w)
		self._horizontal = 2.0 * halfWidth * focusDist * self._u
		self._vertical = 2.0 * halfHeight * focusDist * self._v

	def _randomInUnitDisk(self):
		p = Vec3()
		while True:
			p = 2.0 * Vec3(random(), random(), 0) - Vec3(1, 1, 0)
			if Vec3.dot(p, p) < 1.0:
				break;

		return p

	@property
	def U(self):
		return self._u
	
	@property
	def V(self):
		return self._v

	@property
	def W(self):
		return self._w

	@property
	def LensRadius(self):
		return self._lensRadius

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
		rd = self._lensRadius * self._randomInUnitDisk()
		offset = self._u * rd.X + self._v * rd.Y
		return Ray(self._origin + offset, self._lowerLeftCorner + (s * self._horizontal) + (t * self._vertical) - self._origin - offset)