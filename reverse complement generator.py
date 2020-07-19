def reverse_complement(genome):
	genome = genome.casefold()
	new_genome = genome.replace ("a", "T")
	genome = new_genome
	new_genome = genome.replace ("g", "C")
	genome = new_genome
	new_genome = genome.replace ("c", "G")
	genome = new_genome
	new_genome = genome.replace ("t", "A")
	genome = new_genome
	print (genome[::-1])
	return;

reverse_complement(genome = 'AAAACCCGGT')
# Output --> 'ACCGGGTTTT'
