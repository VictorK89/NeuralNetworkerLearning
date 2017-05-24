import numpy as np

##matrix = np.loadtxt('german_model_vectors.txt', usecols=range(300), dtype=float)
##np.save('german_model_matrix', matrix)


f = open('german_model_vectors.txt', 'r')
g = open('german_model_vectors_converted_float', 'w')

for line in f:
	if line.strip():
		g.write(np.array(map(float, line.split())))

