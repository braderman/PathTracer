from .material import Material
from .vec3 import Vec3
from .ray import Ray
import math
from random import random

class Dielectric(Material):
	def __init__(self, refIdx):
		self._refIdx = refIdx 

	@property
	def RefractiveIndex(self):
		return self._refIdx

	def _schlick(self, cosine):
		r0 = (1.0 - self._refIdx) / (1.0 + self._refIdx)
		r0 = r0 * r0
		return r0 + (1.0 - r0) * math.pow((1.0 - cosine), 5)

	def scatter(self, rIn, rec):
		reflected = Vec3.reflect(rIn.Direction, rec.Normal)
		attentuation = Vec3(1.0, 1.0, 1.0)
		if Vec3.dot(rIn.Direction, rec.Normal) > 0:
			outwardNormal = -rec.Normal
			niOverNt = self._refIdx
			cosine = self._refIdx * Vec3.dot(rIn.Direction, rec.Normal) / rIn.Direction.Length
		else:
			outwardNormal = rec.Normal
			niOverNt = 1.0 / self._refIdx
			cosine = -Vec3.dot(rIn.Direction, rec.Normal) / rIn.Direction.Length

		bRefract, refracted = Vec3.refract(rIn.Direction, outwardNormal, niOverNt)
		if bRefract:
			reflectProb = self._schlick(cosine)
		else:
			reflectProb = 1.0

		if random() < reflectProb:
			scattered = Ray(rec.P, reflected)
		else:
			scattered = Ray(rec.P, refracted)

		return (True, attentuation, scattered)
