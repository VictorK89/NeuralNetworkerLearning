## Victor Krause

import numpy as np

g = open('german_model_wordlist.txt', 'r')
h = open('wordlist_annotations_1', 'r')
i = open('annotations_index_from_embeddings_1', 'w')


with open('wordlist_annotations_1', 'r') as h:
	for line in h:
		p = h.readlines()
		for num, line in enumerate(g):
			if (line.startswith(p + "\n")):
				i.write("%s" % (num)+"\n")
