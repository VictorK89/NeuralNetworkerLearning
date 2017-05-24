# Victor Krause
# getting index from wordlist_annotations from word_embeddings; if not available write -1
# w = # of words not usable because we have no vector of it, write the usable word list

i = open('wordlist_annotations_usable_10', 'w')

w = 0

with open('german_model_wordlist.txt', 'r') as big:
	ix = 0
	word_index = {}

	for line in big:
		word = line.strip()
		if word not in word_index:
			word_index[word] = ix
		ix += 1

with open('wordlist_annotations_10', 'r') as small:
	for line in small:
		word_usable = line.strip()
		if word_usable not in word_index:
			w = w + 1
			#i.write('-1' + "\n")
		else:
			i.write("%s" % word_usable + "\n")
print(w)
