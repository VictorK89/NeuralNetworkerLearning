minus_one = ['-1']

with open('annotations_index_from_embeddings_10', 'r') as oldfile, open('annotations_index_from_embeddings_not_one_10', 'w') as newfile:
	for line in oldfile:
		if not any(minus_one in line for minus_one in minus_one):
			newfile.write(line)
