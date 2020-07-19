def skew_minima (genome):
  skew = 0
  skew_dict = {0:0}
  minima = []
  for i in range (len(genome)):
    if genome[i]=='C':
      skew = skew - 1
      skew_dict[i] = skew
    elif genome[i]=='G':
      skew = skew + 1
      skew_dict[i] = skew
    else:
      skew_dict[i] = skew
  minimum_skew = min(skew_dict.values())
  for j in skew_dict:
    if skew_dict[j] == minimum_skew:
      minima.append(j)
  print (minima)
  return;

skew_minima (genome = 'ATAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT')
# Output --> [11, 24]             
