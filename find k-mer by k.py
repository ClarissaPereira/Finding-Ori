# Finds the most frequent k-mer in a base sequence when given the k-mer length

def find_kmer_by_k (genome, k):
  k_list = []
  k_dict = {}
  for i in range (len(genome)-k+1):
    k_list.append(genome[i:i+k])
  for kmer in k_list:
    kmer_count = k_list.count(kmer)
    k_dict[kmer] = kmer_count
  max_freq = max(k_dict.items(), key = lambda x: x[1])
  frequent_kmers = []
  for key, value in k_dict.items():
    if value == max_freq[1]:
      frequent_kmers.append(key)
  print(frequent_kmers)
  return;

find_kmer_by_k (genome = 'AGTATATC', k = 3)
# Output --> ['TAT'] 
