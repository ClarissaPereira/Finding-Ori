genome = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
k = 5
t = 4
frequent = {}
j = []
counts = {}
position = {}
num = []
for i in range (len(genome)):
    kmer = genome[i:i + k]
    if kmer in counts:
        counts[kmer] += 1
        position.setdefault(kmer, []).append(i)
    else:
        counts[kmer] = 1
        position.setdefault(kmer, []).append(i)
print (counts)
for k in counts:
  	if counts[k] >= t:
          frequent[k] = counts[k]
          #print (counts[k])
print (frequent)
print (position)
for j in frequent:
     if j in position:
         comparisonlist = position[j]
         minimum = min(comparisonlist)
         maximum = max(comparisonlist)
         if (maximum - minimum) <= 50:
             num.append(j)
print (num)
