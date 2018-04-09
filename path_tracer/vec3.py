import math
from random import random

class Vec3:
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		self._e = [float(x), float(y), float(z)]

	def __str__(self):
		return "%f %f %f" % (self._e[0], self._e[1], self._e[2])

	def __repr__(self):
		return "%f %f %f" % (self._e[0], self._e[1], self._e[2])

	def __getitem__(self, key):
		return self._e[key]

	def __setitem__(self, key, value):
		self._e[key] = value

	def __neg__(self):
		return Vec3(-self._e[0], -self._e[1], -self._e[2])

	def __add__(self, other):
		return Vec3(self._e[0] + other._e[0], self._e[1] + other._e[1], self._e[2] + other._e[2])

	def __sub__(self, other):
		return Vec3(self._e[0] - other._e[0], self._e[1] - other._e[1], self._e[2] - other._e[2])

	def __mul__(self, other):
		if isinstance(other, float):
			return Vec3(self._e[0] * other, self._e[1] * other, self._e[2] * other)
		else:
			return Vec3(self._e[0] * other._e[0], self._e[1] * other._e[1], self._e[2] * other._e[2])

	def __rmul__(self, other):
		return Vec3(self._e[0] * other, self._e[1] * other, self._e[2] * other)

	def __truediv__(self, other):
		if isinstance(other, float):
			k = 1.0/other
			return Vec3(self._e[0] * k, self._e[1] * k, self._e[2] * k)
		else:
			return Vec3(self._e[0] / other._e[0], self._e[1] / other._e[1], self._e[2] / other._e[2])

	def __iadd__(self, other):
		self._e[0] += other._e[0]
		self._e[1] += other._e[1]
		self._e[2] += other._e[2]
		return self

	def __isub__(self, other):
		self._e[0] -= other._e[0]
		self._e[1] -= other._e[1]
		self._e[2] -= other._e[2]
		return self

	def __imul__(self, other):
		if isinstance(other, float):
			self._e[0] *= other
			self._e[1] *= other
			self._e[2] *= other
			return self
		else:
			self._e[0] *= other._e[0]
			self._e[1] *= other._e[1]
			self._e[2] *= other._e[2]
			return self

	def __itruediv__(self, other):
		if isinstance(other, float):
			k = 1.0/other
			self._e[0] *= k
			self._e[1] *= k
			self._e[2] *= k
			return self
		else:
			self._e[0] /= other._e[0]
			self._e[1] /= other._e[1]
			self._e[2] /= other._e[2]
			return self			

	@property
	def X(self):
		return self._e[0]

	@property
	def Y(self):
		return self._e[1]

	@property
	def Z(self):
		return self._e[2]

	@property
	def R(self):
		return self._e[0]

	@property
	def G(self):
		return self._e[1]

	@property
	def B(self):
		return self._e[2]

	@property
	def Length(self):
		return math.sqrt(self._e[0] * self._e[0] + self._e[1] * self._e[1] + self._e[2] * self._e[2])

	@property
	def SquaredLength(self):
		return self._e[0] * self._e[0] + self._e[1] * self._e[1] + self._e[2] * self._e[2]

	def makeUnitVector(self):
		k = 1.0 / math.sqrt(self._e[0] * self._e[0] + self._e[1] * self._e[1] + self._e[2] * self._e[2])
		self._e[0] *= k
		self._e[1] *= k
		self._e[2] *= k

	@staticmethod
	def dot(v1, v2):
		return v1._e[0] * v2._e[0] + v1._e[1] * v2._e[1] + v1._e[2] * v2._e[2]

	@staticmethod
	def cross(v1, v2):
		return Vec3(v1._e[1] * v2._e[2] - v1._e[2] * v2._e[1],
			        -(v1._e[0] * v2._e[2] - v1._e[2] * v2._e[0]),
			        v1._e[0] * v2._e[1] - v1._e[1] * v2._e[0])

	@staticmethod
	def unitVector(v):
		return v / v.Length

	@staticmethod
	def randomInUnitSphere():
		while True:
			p = 2.0 * Vec3(random(), random(), random()) - Vec3(1, 1, 1)
			if p.SquaredLength < 1.0:
				break

		return p

	@staticmethod
	def reflect(v, n):
		return v - 2 * Vec3.dot(v, n) * n

