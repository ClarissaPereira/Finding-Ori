# searches for a specific k-mer string within a larger genome
# accounts for overlapping sub-strings
def basic_kmer_search (genome, kmer):
  count = 0
  for i in range (len(genome)-len(kmer)+1):
# genome of length L has (L-k+1) k-mers
    if genome[i:i+k]==kmer:
      count += 1
  print (count)
  return;

basic_kmer_search (genome = 'AGAGAT', kmer = 'AGA')
