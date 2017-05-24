g = open('top_or_not_usable_binary_10_only_zero', 'r')
h= open('actual_zero', 'w')

for line in g:
	if line.rstrip():
		h.write(line)
