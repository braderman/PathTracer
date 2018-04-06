import unittest
from path_tracer import Vec3

class Vec3TestMethods(unittest.TestCase):
	def test_construct(self):
		v = Vec3()
		self.assertEqual(v._e[0], 0)
		self.assertEqual(v._e[1], 0)
		self.assertEqual(v._e[2], 0)

		v = Vec3(1, 2, 3)
		self.assertEqual(v._e[0], 1)
		self.assertEqual(v._e[1], 2)
		self.assertEqual(v._e[2], 3)		

	def test_getter(self):
		v = Vec3()
		self.assertEqual(v[0], 0)
		self.assertEqual(v[1], 0)
		self.assertEqual(v[2], 0)

		v = Vec3(1, 2, 3)
		self.assertEqual(v[0], 1)
		self.assertEqual(v[1], 2)
		self.assertEqual(v[2], 3)		

	def test_setter(self):
		v = Vec3()
		self.assertEqual(v._e[0], 0)
		self.assertEqual(v._e[1], 0)
		self.assertEqual(v._e[2], 0)

		v[0] = 1
		v[1] = 2
		v[2] = 3

		self.assertEqual(v._e[0], 1)
		self.assertEqual(v._e[1], 2)
		self.assertEqual(v._e[2], 3)	

	def test_properties(self):
		v = Vec3(1, 2, 3)
		self.assertEqual(v.X, 1)
		self.assertEqual(v.Y, 2)
		self.assertEqual(v.Z, 3)		
		self.assertEqual(v.R, 1)
		self.assertEqual(v.G, 2)
		self.assertEqual(v.B, 3)

	def test_neg(self):
		v = Vec3(1, 2, 3)
		self.assertEqual(v[0], 1)
		self.assertEqual(v[1], 2)
		self.assertEqual(v[2], 3)

		w = -v				
		self.assertEqual(w[0], -1)
		self.assertEqual(w[1], -2)
		self.assertEqual(w[2], -3)

	def test_str(self):
		v = Vec3(1, 2, 3)
		self.assertEqual(str(v), "1.000000 2.000000 3.000000")

	def test_add(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v3 = v1 + v2
		self.assertEqual(v3[0], 5)
		self.assertEqual(v3[1], 7)
		self.assertEqual(v3[2], 9)		

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 5)
		self.assertEqual(v2[2], 6)		

	def test_add_equals(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v1 += v2
		self.assertEqual(v1[0], 5)
		self.assertEqual(v1[1], 7)
		self.assertEqual(v1[2], 9)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 5)
		self.assertEqual(v2[2], 6)		

	def test_sub(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v3 = v2 - v1
		self.assertEqual(v3[0], 3)
		self.assertEqual(v3[1], 3)
		self.assertEqual(v3[2], 3)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 5)
		self.assertEqual(v2[2], 6)		

	def test_sub_equals(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v2 -= v1
		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 3)
		self.assertEqual(v2[1], 3)
		self.assertEqual(v2[2], 3)		

	def test_mul_vector(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v3 = v1 * v2
		self.assertEqual(v3[0], 4)
		self.assertEqual(v3[1], 10)
		self.assertEqual(v3[2], 18)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 5)
		self.assertEqual(v2[2], 6)		

	def test_mul_vector_equals(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 5, 6)
		v1 *= v2
		self.assertEqual(v1[0], 4)
		self.assertEqual(v1[1], 10)
		self.assertEqual(v1[2], 18)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 5)
		self.assertEqual(v2[2], 6)		

	def test_mul_scalar(self):
		v1 = Vec3(1, 2, 3)
		v2 = v1 * 2.0
		self.assertEqual(v2[0], 2)
		self.assertEqual(v2[1], 4)
		self.assertEqual(v2[2], 6)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

	def test_mul_scalar_equals(self):
		v1 = Vec3(1, 2, 3)
		v1 *= 2.0
		self.assertEqual(v1[0], 2)
		self.assertEqual(v1[1], 4)
		self.assertEqual(v1[2], 6)		

	def test_mul_scalar_reflected(self):
		v1 = Vec3(1, 2, 3)
		v2 = 2.0 * v1
		self.assertEqual(v2[0], 2)
		self.assertEqual(v2[1], 4)
		self.assertEqual(v2[2], 6)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

	def test_div_vector(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 6, 6)
		v3 = v2 / v1
		self.assertEqual(v3[0], 4)
		self.assertEqual(v3[1], 3)
		self.assertEqual(v3[2], 2)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 6)
		self.assertEqual(v2[2], 6)		

	def test_div_vector_equals(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 6, 6)
		v2 /= v1
		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

		self.assertEqual(v2[0], 4)
		self.assertEqual(v2[1], 3)
		self.assertEqual(v2[2], 2)		

	def test_div_scalar(self):
		v1 = Vec3(1, 2, 3)
		v2 = v1 / 0.5
		self.assertEqual(v2[0], 2)
		self.assertEqual(v2[1], 4)
		self.assertEqual(v2[2], 6)

		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

	def test_div_scalar_equals(self):
		v1 = Vec3(1, 2, 3)
		v1 /= 0.5
		self.assertEqual(v1[0], 2)
		self.assertEqual(v1[1], 4)
		self.assertEqual(v1[2], 6)		

	def test_length(self):
		v = Vec3(1, 2, 3)
		self.assertEqual(v.Length, 3.7416573867739413)
		self.assertEqual(v.SquaredLength, 14)

	def test_dot(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3(4, 6, 6)
		self.assertEqual(Vec3.dot(v1, v2), 34)

	def test_makeunitvector(self):
		v = Vec3(1, 2, 3)
		v.makeUnitVector()
		self.assertEqual(v.Length, 1)
		self.assertEqual(v.SquaredLength, 1)
		self.assertEqual(v[0], 0.2672612419124244)
		self.assertEqual(v[1], 0.5345224838248488)
		self.assertEqual(v[2], 0.8017837257372732)		

	def test_unitvector(self):
		v1 = Vec3(1, 2, 3)
		v2 = Vec3.unitVector(v1)
		self.assertEqual(v2.Length, 1)
		self.assertEqual(v2.SquaredLength, 1)
		self.assertEqual(v2[0], 0.2672612419124244)
		self.assertEqual(v2[1], 0.5345224838248488)
		self.assertEqual(v2[2], 0.8017837257372732)		
		self.assertEqual(v1[0], 1)
		self.assertEqual(v1[1], 2)
		self.assertEqual(v1[2], 3)		

	def test_cross(self):
		v1 = Vec3(1, 0, 0)
		v2 = Vec3(0, 1, 0)
		v3 = Vec3.cross(v1, v2)
		self.assertEqual(v3[0], 0)
		self.assertEqual(v3[1], 0)
		self.assertEqual(v3[2], 1)		


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Vec3TestMethods)
	unittest.TextTestRunner(verbosity=2).run(suite)