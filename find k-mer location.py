# Given both the genome and the specific k-mer string, this function find the locations within the genome where the k-mer appears
def locate_kmer (genome, kmer): 
  location_list = []
  for i in range (len(genome)-len(kmer)+1):
    if genome[i:i+len(kmer)] == kmer:
      location_list.append(i)
  print (location_list, sep = ' ')
  return;

locate_kmer (genome = 'AGCATCATG', kmer = 'CAT')
# Output --> [2, 5]
