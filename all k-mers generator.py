# a Cartesian Product function which generates all possible k-mers when given k 

def all_kmers (k):
  import itertools
  bases = 'AGCT'
  kmers = itertools.product(bases, repeat = 5)
  kmer_list = list(''.join(w) for w in list(kmers))
  print (kmer_list)
  return;

all_kmers(k = 3)
# Output -> ['AAA', 'AAC', 'AAG', ..., 'TTG', 'TTT']

# ALT #
# Came up with a better way to do this whilst working in Tick-TOC1 repo
# slightly more efficient and better readability
import itertools
def all_kmers(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))
