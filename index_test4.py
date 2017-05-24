# Victor Krause
# getting only usable lines from wordlist / topornot list via minus_one_index / vectors

import linecache

w = 0

a = open('nomen_list_usable_8', 'w')

with open ('index_minus_one_annotations_index_from_embeddings_8', 'r') as index:
	int_index = [int(i) for i in index.readlines()]

	for line in int_index:
		w = w + 1
		a.write(linecache.getline('nomen_annotations_8', line))


num_lines = sum(1 for line in open('nomen_list_usable_8', 'r'))


print(len(int_index), w, num_lines)
