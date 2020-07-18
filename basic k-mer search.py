genome = ''
kmer = ''
count = 0
for i in range (len(genome)-len(kmer)+1):
  if genome[i:i+k]==kmer:
    count += 1
print (count)
