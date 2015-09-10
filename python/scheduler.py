from quicksect import IntervalNode
from classroom import Classroom

def find(start, end, tree):
	'''Returns a list with the overlapping intervals'''
	out = []
	tree.contains( start, end, lambda x: out.append(x) )
	return [ (x.start, x.end, x.other) for x in out ]

#Salon 1
sch = {1:[(930,1030),(1130,1230),(1345,1600)],2:[800,900]}
s1 = Classroom("S1", 50,sch)

#Salon 2
sch = {1:[(730,1000),(1350,1500),(1600,1800)],2:[1000,1500]}
s2 = Classroom("S2", 30,sch)

weekTrees = {}

mondayTree = IntervalNode( s1.schedule[1][0][0],s1.schedule[1][0][1],other=s1)

for interval in s1.schedule[1][1:]:
	#print interval
	mondayTree = mondayTree.insert( interval[0],interval[1],other=s1 )

for interval in s2.schedule[1]:
	#print interval
	mondayTree = mondayTree.insert( interval[0],interval[1],other=s2 )
	
print "Results"
start = 1400
end = 1500
overlap = find(start, end , mondayTree)
#print '(%s, %s) -> %s' % (start, end,  overlap[0][2].code + " hora: "+ str(overlap[0][0]) + "," +str(overlap[0][1]) if len(overlap) > 0 else None)
print '(%s, %s) -> %s' % (start, end,  overlap)	