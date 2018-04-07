from .vec3 import Vec3

class Ray:
	def __init__(self, origin = Vec3(), direction = Vec3()):
		self._origin = origin
		self._direction = direction

	@property
	def Origin(self):
		return self._origin

	@property
	def Direction(self):
		return self._direction

	def pointAtParameter(self, t):
		return self._origin + (t * self._direction)


