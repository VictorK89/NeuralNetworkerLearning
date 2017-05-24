## Victor Krause
## used to split to wordlist and vectors
## rip 608130 300

f = open("german_model_converted.txt", "r")
g = open("german_model_vectors.txt", "w")
##h = open("german_model_wordlist.txt", "w")

for line in f:							## vectors
	if line.strip():
		g.write(" ".join(line.split()[1:]) + "\n")



##for line in f:							## wordlist
##	if line.strip():
##		h.write("".join(line.split()[:1]) + "\n")
f.close()
g.close()
#h.close()
