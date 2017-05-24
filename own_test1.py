## Victor Krause
## Working with Annotations

import theanets
import numpy as np, re, theanets
import nltk
from operator import itemgetter

position = []									## create some lists
word = []
blank_one = []
basicword = []
blank_two = []
sign = []
blank_three = []
wordclass = []
number_one = []
number_two = []
blank_four = []
most_nk = []
blank_five = []
blank_six = []
topornotfake = []
topornot = []


with open('train_data10.conll') as infile, open('output.txt', 'w') as outfile:	## open the file and remove blank lines
       for line in infile:							## and rename / save it
              if not line.strip(): continue					## needed because its causing an error
              outfile.write(line)

f = open('output.txt', 'r+w').readlines()					## read the file without blank lines now


position = ( [x.split('	')[0] for x in f] )					## get the position
word = ( [x.split('	')[1] for x in f] )					## get the word
blank_one = ( [x.split('	')[2] for x in f] )
basicword = ( [x.split('	')[3] for x in f] )				## get the basic word
blank_two = ( [x.split('	')[4] for x in f] )				
sign = ( [x.split('	')[5] for x in f] )					## get some sign
blank_three = ( [x.split('	')[6] for x in f] )
wordclass = ( [x.split('	')[7] for x in f] )				## get wordclass
number_one = ( [x.split('	')[8] for x in f] )
number_two = ( [x.split('	')[9] for x in f] )
blank_four = ( [x.split('	')[10] for x in f] )
most_nk = ( [x.split('	')[11] for x in f] )
blank_five = ( [x.split('	')[12] for x in f] )
blank_six = ( [x.split('	')[13] for x in f] )
			
topornotfake = ( [x.split('	')[14] for x in f] )				## get top/notop column with bad \n
				
topornot = map(lambda each:each.strip("\n"), topornotfake)			## top/notop column without \n


with open('nomen_annotations_10', 'w') as h:					## save the wordlist
	for line in sign:
		h.write(line + "\n")

#with open('wordlist_annotations_10', 'w') as j:
#	for line in word:
#		j.write(line + "\n")


## all columns except top/notop
#outcomenotop = [str(position[i]) + " " + str(word[i]) + " " + str(blank_one[i]) + " " + str(basicword[i]) + " " + str(blank_two[i]) + " " + str(sign[i]) + " " + str(blank_three[i]) + " " + str(wordclass#[i]) + " " + str(number_one[i]) + " " + str(number_two[i]) + " " + str(blank_four[i]) + " " + str(most_nk[i]) + " " + str(blank_five[i]) + " " + str(blank_six[i]) for i in range(len(position))]



## all columns
#outcome = [str(position[i]) + " " + str(word[i]) + " " + str(blank_one[i]) + " " + str(basicword[i]) + " " + str(blank_two[i]) + " " + str(sign[i]) + " " + str(blank_three[i]) + " " + str(wordclass[i]) + " " + str(number_one[i]) + " " + str(number_two[i]) + " " + str(blank_four[i]) + " " + str(most_nk[i]) + " " + str(blank_five[i]) + " " + str(blank_six[i]) + " " + str(topornot[i]) for i in range(len(position))]



## theanets part


#model = theanets.Regressor([10,20,3])

#inputs = position
#outputs =   

#model.train([inputs, outputs])

#test = open('test_data_without_top', 'r').readlines()




#print()

