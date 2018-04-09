from .material import Material 
from .vec3 import Vec3
from .ray import Ray

class Lambertian(Material):
	def __init__(self, albedo):
		self._albedo = albedo

	@property
	def Albedo(self):
		return self._albedo

	def scatter(self, rIn, rec):
		target = rec.P + rec.Normal + Vec3.randomInUnitSphere()
		scattered = Ray(rec.P , target - rec.P)
		return (True, self._albedo, scattered)