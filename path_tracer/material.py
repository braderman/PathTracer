from .hitable import HitRecord

class Material:
	def scatter(self, rIn, rec):
		#bScattered, Attenuation Vector, Scattered Ray
		return (False, None, None)