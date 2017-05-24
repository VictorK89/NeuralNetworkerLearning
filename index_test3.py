# Victor Krause
# get all index with not -1 because they are useless

i = open('index_minus_one_annotations_index_from_embeddings_10', 'w')

with open('annotations_index_from_embeddings_10', 'r') as big:
	for num, line in enumerate(big, 1):
		if not "-1" in line:
			i.write("%i" % num + '\n')
