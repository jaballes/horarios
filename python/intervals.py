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
				res.append((interval,idx))
		return res
	def remove(self, start, end, obj, level):
		idx = 0
		for interval in self.levels[level]:
			s, e, to = interval
			if to == obj:  # same object
				del self.levels[level][idx]
				if s <= start <= end <= e:
					
			idx += 1
		