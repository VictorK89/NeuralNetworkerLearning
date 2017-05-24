import numpy as np

f = open("german_model_converted.txt", "r")
g = open("german_model_vectors.txt", "w")

for line in f:
	if line.strip():
		g.write("\t".join(line.split()[1:]))
