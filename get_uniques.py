g = open("nomen_annotations_9", "r")

uniquewords = []

for i in g:
	if not i in uniquewords:
		uniquewords.append(i);

print(len(uniquewords))
print(uniquewords)
