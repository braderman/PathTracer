import sys
from path_tracer import Vec3, Ray

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

def color(r):
	unitDirection = Vec3.unitVector(r.Direction) # unitDiection x and y will be between -1 and 1
	t = 0.5 * (unitDirection.Y + 1.0) # scale t -> 0 < t < 1
	return (1.0 - t) * Vec3(1.0, 1.0, 1.0) + t * Vec3(0.5, 0.7, 1.0) #lerp between white and blue

def main():
	nx = 200
	ny = 100
	print("P3\n%d %d\n255" % (nx, ny))
	lowerLeftCorner = Vec3(-2.0, -1.0, -1.0)
	horizontal = Vec3(4.0, 0.0, 0.0)
	vertical = Vec3(0.0, 2.0, 0.0)
	origin = Vec3(0.0, 0.0, 0.0)

	for j in reversed(range(ny)):
		for i in range(nx):
			u = i / float(nx)
			v = j / float(ny)
			r = Ray(origin, lowerLeftCorner + (u * horizontal) + (v * vertical))
			col = color(r)
			ir = int(255.99 * col.R)
			ig = int(255.99 * col.G)
			ib = int(255.99 * col.B)
			print("%d %d %d" % (ir, ig, ib))


if __name__ == '__main__':
	main()