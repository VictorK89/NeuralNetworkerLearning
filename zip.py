combine = []

with open('nomen_replaced_8', 'r') as xh:
	with open('vector_list_usable_8', 'r') as yh:
		with open('vector_nomen_8', 'w') as zh:
			xlines = xh.readlines()
			ylines = yh.readlines()
			
			for line1, line2 in zip(ylines, xlines):
				zh.write('{} {}\n'.format(line1.rstrip(), line2.rstrip()))
