class IntervalList:
	def __init__( self, nlevels ):
		self.nlevels = nlevels
		self.levels = {}
		for i in xrange(1,nlevels):
			self.levels[i] = []
	def insert(self, start, end, obj, level):
		if not self.levels[level]:
			self.levels[level] = []
		self.levels[level].append((start,end,obj))
	def find(self, start, end, level):
		res = []
		for interval in self.levels[level]:
			s, e, obj = interval
			if s <= start <= end <= e:
				res.append(interval)
		return res
	def remove(self, start, end, obj, level):
		idx = 0
		for interval in self.levels[level]:
			s, e, to = interval
			if to == obj:  # same object
				if s <= start <= end <= e:
					del self.levels[level][idx]
					bi = start - s
					en = e - end
					if bi > 0:
						print "bi" 
						self.insert(s, start, obj, level)
					if en > 0:
						print "en"
						self.insert(end, e, obj, level)
			idx +=1

		