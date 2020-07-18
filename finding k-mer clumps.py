# Find frequent k-mers that cluster together into clumps in the genome
# inputs are:    genome 
#                k (the length of the k-mer) 
#                L (the maximum length of a clump region)
#                t (the minimum frequency of a k-mer in the clump)  
def kmer_clump_finder (genome, k, t, L):
    frequent_kmers = {}
    kmer_count = {}
    kmer_position = {}
    clump_forming_kmers = []
    for i in range (len(genome)):
        kmer = genome[i:i + k]
        if kmer in kmer_count:
            kmer_count[kmer] += 1
            kmer_position.setdefault(kmer, []).append(i)
        else:
            kmer_count[kmer] = 1
            kmer_position.setdefault(kmer, []).append(i)
    for k in kmer_count:
  	    if kmer_count[k] >= t:
            frequent_kmers[k] = kmer_count[k]
    for j in frequent_kmers:
        if j in kmer_position:
            position_range = kmer_position[j]
            minimum = min(position_range)
            maximum = max(position_range)
            if (maximum - minimum) <= L:
                clump_forming_kmers.append(j)
# checks if all positions of the frequent k-mer cluster within a clump region of maximum length L 
    print (clump_forming_kmers)
    return;

kmer_clump_finder(genome = 'CGGACTCGACAGATGTGAAGAACGA', k=3, t=2, L=10) 
# Output --> ['GAC', 'AGA', 'GAA']
