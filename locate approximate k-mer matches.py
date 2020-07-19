# similar to the locate_kmer function (see https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20k-mer%20location.py)
# but also accounts for approximate pattern matches resulting from mutations in DNA base sequence

def locate_imperfect_kmer (genome, kmer, d):
  position = []
  for i in range (len(genome) - len(kmer) + 1):
    test_string = genome[i:i+len(kmer)]
    if test_string == kmer:
      position.append(i)
    else:
      hamming_distance (sequence1 = kmer, sequence2 = test_string)
# hamming_distance function can be found here: https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20mutated%20bases.py
# d = maximum hamming distance tolerated
      if hamming <= d:
        position.append(i)
  print (position)
  return;

locate_imperfect_kmer (genome = 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT', kmer = 'ATTCTGGA', d = 3)
# Output -> [6, 7, 26, 27]
  
      
