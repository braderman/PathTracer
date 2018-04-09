from .hitable import HitRecord

class Material:
	def scatter(self, r, rec):
		#bScattered, Attenuation Vector, Scattered Ray
		return (False, None, None)