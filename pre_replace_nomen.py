replacements = {'PTKNEG':'OBAMA',
                'APPRART':'TRUMP'}

with open('nomen_list_usable_8', 'r') as infile, open('nomen_pre_replaced_8', 'w') as outfile:
        for line in infile:
                for src, target in replacements.iteritems():
                        line = line.replace(src, target)
                outfile.write(line)

