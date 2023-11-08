# READ ME
# This program will take in one FASTA file and split the file into multiple files based on their label.
# In the multi FASTA file, each label should have the following format:
# > ID Contig .......
# The new files will be named after the ID in the label and all labels that contain the ID will be included
# in the new file. The new labels in the file will have the following format:
# > Contig .....

def splitFasta(file):
	f = open(file, 'r')
	info = f.readlines()

	new_files = dict()
	for line in info:
		if '>' in line:
			try:
				if ID in new_files:
					new_files[ID].append(data)
				else:
					new_files[ID] = []
					new_files[ID].append(data)
			except:
				pass

			data = []
			line = line.strip('>').strip(' ').split()
			ID = line[0]
			contig = ''
			for i in line[1:]:
				contig += i + ' '
			data.append(contig)
		else:
			data.append(line)

	#get the last label
	if ID in new_files:
		new_files[ID].append(data)
	else:
		new_files[ID] = []
		new_files[ID].append(data)

	for ID in new_files:
		f = open(ID + '.fasta', 'w')
		for data in new_files[ID]:
			label = data[0].strip(' ')
			f.write('>' + label + '\n')
			for line in data[1:]:
				f.write(line)
		f.close()

if __name__ == '__main__':
	file = input('Enter FASTA file that you want to split: ')

	splitFasta(file)