from .hitable import Hitable, HitRecord
from .vec3 import Vec3 
import math

class Sphere(Hitable):
	def __init__(self, center = Vec3(), radius = 0.0):
		self._center = center
		self._radius = float(radius) 

	@property
	def Center(self):
		return self._center 

	@property
	def Radius(self):
		return self._radius

	def _createHitRecord(self, r, temp):
		t = temp
		p = r.pointAtParameter(t)
		normal = (p - self._center) / self._radius
		return HitRecord(t, p, normal)

	def hit(self, r, tmin, tmax):
		oc = r.Origin - self._center
		a = Vec3.dot(r.Direction, r.Direction)
		b = Vec3.dot(oc, r.Direction)
		c = Vec3.dot(oc, oc) - self._radius * self._radius
		discriminant = b * b - a * c
		if discriminant > 0:
			discrimSqRoot = math.sqrt(discriminant)
			temp = (-b - discrimSqRoot)/a
			if temp < tmax and temp > tmin:
				return (True, self._createHitRecord(r, temp))

			temp = (-b + discrimSqRoot)/a
			if temp < tmax and temp > tmin:
				return (True, self._createHitRecord(r, temp))

		return (False, None)