import sys
import math
from path_tracer import Vec3, Ray, Sphere, HitableList, Camera
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

def color(r, world):
	bHit, rec = world.hit(r, 0.0, sys.float_info.max)
	if bHit:
		return 0.5 * Vec3(rec.Normal.X+1, rec.Normal.Y+1, rec.Normal.Z+1)
	else:
		unitDirection = Vec3.unitVector(r.Direction)
		t = 0.5 * (unitDirection.Y + 1.0)
		return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0)

def main():
	nx = 200
	ny = 100
	ns = 100
	print("P3\n%d %d\n255" % (nx, ny))

	world = HitableList()
	world.append(Sphere(Vec3(0.0, 0.0, -1.0), 0.5))
	world.append(Sphere(Vec3(0.0, -100.5, -1.0), 100.0))

	cam = Camera()

	for j in reversed(range(ny)):
		for i in range(nx):
			col = Vec3(0.0, 0.0, 0.0)
			for s in range(ns):
				u = (i + random()) / float(nx)
				v = (j + random()) / float(ny)
				r = cam.getRay(u, v)
				col += color(r, world)

			col /= float(ns)	
			ir = int(255.99 * col.R)
			ig = int(255.99 * col.G)
			ib = int(255.99 * col.B)
			print("%d %d %d" % (ir, ig, ib))


if __name__ == '__main__':
	main()