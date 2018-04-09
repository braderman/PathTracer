from .material import Material
from .ray import Ray
from .vec3 import Vec3

class Metal(Material):
	def __init__(self, albedo, fuzz):
		self._albedo = albedo
		if fuzz < 1:
			self._fuzz = float(fuzz)
		else:
			self._fuzz = 1.0

	@property
	def Albedo(self):
		return self._albedo

	@property
	def Fuzz(self):
		return self._fuzz

	def scatter(self, rIn, rec):
		reflected = Vec3.reflect(Vec3.unitVector(rIn.Direction), rec.Normal)
		scattered = Ray(rec.P, reflected + self._fuzz * Vec3.randomInUnitSphere())
		return (Vec3.dot(scattered.Direction, rec.Normal) > 0, self._albedo, scattered)
