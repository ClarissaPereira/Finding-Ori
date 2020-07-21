# Because of deamination mutations, some DnaA boxes will have one changed nucleotide but DnaA protein can stil bind to variations of the DnaA box sequence
# This function identifies the number of mutations between an original and replicated strand of DNA by calculating Hamming distance

def hamming_distance (sequence1, sequence2):
  hamming = 0
  for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
      hamming += 1
  print (hamming)
  return;

hamming_distance (sequence1 = 'AGCTATAGC', sequence2 = 'AGCTGTGAC')
# Output -> 3

# ALT # 
# Can be made more efficient by zipping sequence 1 and sequence 2 into a tuple
# And more readable by using the sum function instead of incrementing hamming iteratively 
def hamming_distance(pattern, seq):
    return sum(pattern_base1 != pattern_base2 for pattern_base1, pattern_base2 in zip(pattern, seq))
