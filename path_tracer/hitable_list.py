from .hitable import Hitable

class HitableList(Hitable):
	def __init__(self):
		self._list = []

	def __len__(self):
		return len(self._list)

	def __iter__(self):
		return iter(self._list)

	def append(self, hitable):
		self._list.append(hitable)

	def hit(self, r, tmin, tmax):
		hitAnything = False
		closestSoFar = tmax
		retRec = None
		for hitable in self._list:
			bHit, rec = hitable.hit(r, tmin, closestSoFar)
			if bHit:
				hitAnything = True
				closestSoFar = rec.T
				retRec = rec

		return (hitAnything, retRec)
