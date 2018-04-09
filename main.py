import sys
import math
from path_tracer import Vec3, Ray, Sphere, HitableList, Camera, Lambertian, Metal
from random import random

def testImage():
	nx = 200
	ny = 100
	print("P3\n%d %d\n255" % (nx, ny))
	for j in reversed(range(ny)):
		for i in range(nx):
			col = Vec3(i / float(nx), j / float(ny), 0.2)
			ir = int(255.99 * col.R)
			ig = int(255.99 * col.G)
			ib = int(255.99 * col.B)
			print("%d %d %d" % (ir, ig, ib))

def color(r, world, depth):
	bHit, rec = world.hit(r, 0.001, sys.float_info.max)
	if bHit:
		if depth < 50:
			bScattered, attenuation, scattered = rec.Material.scatter(r, rec)
			if bScattered:
				return attenuation * color(scattered, world, depth + 1)
			else:
				return Vec3(0, 0, 0)
		else:
			return Vec3(0, 0, 0)
	else:
		unitDirection = Vec3.unitVector(r.Direction)
		t = 0.5 * (unitDirection.Y + 1.0)
		return (1.0 - t) * Vec3(1, 1, 1) + t * Vec3(0.5, 0.7, 1.0)

def main():
	nx = 200
	ny = 100
	ns = 100
	print("P3\n%d %d\n255" % (nx, ny))

	world = HitableList()
	world.append(Sphere(Vec3(0, 0, -1), 0.5, Lambertian(Vec3(0.8, 0.3, 0.3))))
	world.append(Sphere(Vec3(0, -100.5, -1), 100, Lambertian(Vec3(0.8, 0.8, 0.0))))
	world.append(Sphere(Vec3(1, 0, -1), 0.5, Metal(Vec3(0.8, 0.6, 0.2), 1.0)))
	world.append(Sphere(Vec3(-1, 0, -1), 0.5, Metal(Vec3(0.8, 0.8, 0.8), 0.3)))

	cam = Camera()

	for j in reversed(range(ny)):
		for i in range(nx):
			col = Vec3(0.0, 0.0, 0.0)
			for s in range(ns):
				u = (i + random()) / float(nx)
				v = (j + random()) / float(ny)
				r = cam.getRay(u, v)
				col += color(r, world, 0)

			col /= float(ns)
			col = Vec3(math.sqrt(col.R), math.sqrt(col.G), math.sqrt(col.B))	
			ir = int(255.99 * col.R)
			ig = int(255.99 * col.G)
			ib = int(255.99 * col.B)
			print("%d %d %d" % (ir, ig, ib))


if __name__ == '__main__':
	main()