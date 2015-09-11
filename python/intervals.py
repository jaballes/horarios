class IntervalList:
	def __init__( self, nlevels ):
		self.nlevels = nlevels
		self.levels = {}
	def insert(self, start, end, obj, level):
		self.levels[level].append((start,end,obj))