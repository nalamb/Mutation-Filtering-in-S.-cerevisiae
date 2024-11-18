#Edited to filter variants from WT vcf files and determine unique mutations
#Read in two files
#Write out unique variants and common variants
import sys

PE2ref = sys.argv[1]
PE2var = sys.argv[2]
unique = sys.argv[3]
common = sys.argv[4]


with open(PE2var, "r") as fin, open(PE2ref, "r") as fin2, open(unique, "w") as fout, open(common, "w") as fout2:
	lines = fin.readlines()
	lines2 = fin2.readlines()
	for line in lines:
		counter = 0
		for line2 in lines2:
			col = line.split('\t')
			col2 = line2.split('\t')
			if col[0] == col2[0]:
				if col[1] == col2[1]:
					if col[3] == col2[3]:
						if col[4] == col2[4]:
							counter += 1
		if counter == 0:
			fout.write(line)
		if counter == 1:
			fout2.write(line)

fin.close()
fin2.close()
fout.close()
fout2.close()
