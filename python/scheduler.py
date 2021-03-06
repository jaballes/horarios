from copy import deepcopy
from quicksect import IntervalNode
from classroom import Classroom
from intervals import IntervalList

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

tuesdayTree = deepcopy(mondayTree)
ilist = IntervalList(5)
#interval list
for interval in s1.schedule[1]:
	ilist.insert(interval[0],interval[1],s1,1)

for interval in s2.schedule[1]:
	ilist.insert(interval[0],interval[1],s2,1)
	
print "Results"
start = 730
end = 800
overlap = find(start, end , tuesdayTree)
#print '(%s, %s) -> %s' % (start, end,  overlap[0][2].code + " hora: "+ str(overlap[0][0]) + "," +str(overlap[0][1]) if len(overlap) > 0 else None)
print '(%s, %s) -> %s' % (start, end,  overlap)	

overlap = find(start, end , mondayTree)
#print '(%s, %s) -> %s' % (start, end,  overlap[0][2].code + " hora: "+ str(overlap[0][0]) + "," +str(overlap[0][1]) if len(overlap) > 0 else None)
print '(%s, %s) -> %s' % (start, end,  overlap)

print "With interval list"

overlap = ilist.find(start, end , 1)
print '(%s, %s) -> %s' % (start, end,  overlap)
overlap = ilist.remove(start, end , overlap[0][2],1)
overlap = ilist.find(start, end , 1)
print '(%s, %s) -> %s' % (start, end,  overlap)
start = 830
end = 900
overlap = ilist.find(start, end , 1)
print '(%s, %s) -> %s' % (start, end,  overlap)