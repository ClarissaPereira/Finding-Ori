# This program identifies the most frequent k-mer clumps in the origin of replication region of the genome  
# It takes three inputs --> a full bacterial genome, k, and d (the tolerance for mutations/ mismatches)
# It takes into account reverse complements and mutated variations of the k-mer

## uses skew_minima function to obtain predicted ori position
## widens search window - starts 250 positions before ori and ends 249 positions after - k-mers clustered in this region are considered as a clump
## adds k-mers found in window to a list using genome[i:i+k] and the reverse_complement function
## for each k-mer in the list, uses the hamming_distance function to identify all its mutated versions (uses all_kmers)
## appends all the mutated versions to the list
## uses the Counter function (from collections) to identify most frequent k-mer

senterica = open("S_enterica_genome.txt", "r")
d = 1
k = 9
# search for 9-mers since DnaA boxes tend to be 9 nucleotides in length
kmer_list = []

skew_minima (genome = senterica)

start_position = min(minima) - 250
end_position = max(minima) + 249

clump = genome[start_position:end_position]
for i in clump:
  pattern = clump[i:i+k]
  kmer_list.append(pattern)
  reverse_complement(genome = pattern)
  kmer_list.append(new_genome[::-1])

all_list = []  
all_list.append (all_kmers (k=9))

for i in kmer_list:
  for j in all_list:
    if i == j:
      kmer_list.append(j)
    else:
      hamming_distance (sequence1 = i, sequence2 = j)
      if hamming <= d:
        kmer_list.append(j)
        
from collections import Counter
counts = Counter(kmer_list)
most_frequent_kmer = max(counts, key=counts.get)

print(most_frequent_kmer)
# Output -> 'TTATCCACA'
    
     
  
  
