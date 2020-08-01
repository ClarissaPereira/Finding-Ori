# Finding-Ori
A repository of Python solutions to the code challenges from Unit 1 of Bioinformatics Algorithms (Stepik).

Before opening the code files, I recommend quickly reading about the [biology background of this project](https://github.com/ClarissaPereira/Finding-Ori/blob/master/Biology%20Notes.md) to get a clearer sense of the purpose of each program/function. 

The majority of the files in this repo are for a single function. Most of these small functions contribute to the larger [Final DnaA Box Finder](https://github.com/ClarissaPereira/Finding-Ori/blob/master/Final%20DnaA%20Box%20Finder.py) program. 

The [*Salmonella enterica* genome](https://github.com/ClarissaPereira/Finding-Ori/blob/master/S_enterica_genome.txt) is included as test data. The final DnaA Box Finder identified the S. enterica DnaA box as **TTATCCACA**. An existing [UniProt database entry](https://www.uniprot.org/uniprot/G5S336) confirms that the DnaA sequence is 5'-TTATC[CA]A[CA]A-3' - a successful match!  

## K-mer Searching Functions
* [Find the number of times a k-mer appears in the genome](https://github.com/ClarissaPereira/Finding-Ori/blob/master/basic%20k-mer%20search.py)
* [Find the most frequent k-mer in a genome given the k value](https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20k-mer%20by%20k.py)
* [Find the location of a specific k-mer in a genome](https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20k-mer%20location.py)
* [Find frequent k-mers that cluster together into clumps in the genome](https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20k-mer%20clumps.py)

## Generators
* [Reverse Complement Generator](https://github.com/ClarissaPereira/Finding-Ori/blob/master/reverse%20complement%20generator.py)
* [Generate all possible k-mers](https://github.com/ClarissaPereira/Finding-Ori/blob/master/all%20k-mers%20generator.py)

## Skew Functions
* [Find the minima of a skew plot](https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20skew%20minima.py)
* [NEW -> Plotting skew with Matplotlib](https://github.com/ClarissaPereira/Finding-Ori/blob/master/skew%20plotter.py)

![skewplotex](https://user-images.githubusercontent.com/68158694/87874378-4911dd00-c9c1-11ea-885a-94aab51bd3cd.png)

## Mutations & Imperfect Pattern Matching Functions
* [Find the number of mutated bases in a replicated DNA strand](https://github.com/ClarissaPereira/Finding-Ori/blob/master/find%20mutated%20bases.py)
* [Locate approximate k-mer matches](https://github.com/ClarissaPereira/Finding-Ori/blob/master/locate%20approximate%20k-mer%20matches.py)
