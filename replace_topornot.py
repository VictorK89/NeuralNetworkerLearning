f = open('top_or_not_usable_binary_10', 'r')
g = open('top_or_not_usable_binary_10_only_zero', 'w')

for line in f:
	g.write(line.replace('1', ''))

#for line in f:
#	g.write(line.replace('NOTOP', '0 1'))
