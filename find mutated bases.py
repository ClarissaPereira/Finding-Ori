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
