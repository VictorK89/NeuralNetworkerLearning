## Victor Krause
## Working with GermanWordEmbeddings

import numpy as np

word_vector_list = []
word_vector_list_fake = []

g = open('german_model_vectors.txt', 'r')
h = open('german_model_vectors_eachelements.txt', 'w')
##f = g.readlines()	


for line in g:
		h.write( [x.split(' ') for x in g] )

##word_vector_list_fake = ( [x.split(' ') for x in f] )	## get the vector list and each one is an element; still need to remove \n

##word_vector_list = [[x.replace("\n","") for x in l] for l in word_vector_list_fake] ## needed to remove \n in element of list of lists



##vector_list_bad = np.array(word_vector_list)		## convert list into numpy array


##vector_list_float = vector_list.astype(np.float)

##np.save('vector_list', 'vector_list')			## save vector_list as numpy array, maybe needed later?


##with open('wordlist_embeddings', 'w') as h:		## save the wordlist
##	for line in word_list:
##		h.write(line + "\n")



##for i in range(0, len(vector_list)):			## going from 0 to length of lines
##	print(vector_list[i-1])				## previous line
##	print(vector_list[i])				## actual line
##	print(vector_list[i+1])				## next line


