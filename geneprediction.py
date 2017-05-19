'''
    Build version 1.0.0.0:

    What it can do:
    Check for a promoter from a large list (millions of entries)
    Check for the inclusion of a TATA box
    Check for Start and Stop codon
    Check for GC content in the assumed gene (after the start codon)

    To do:
    Check subsequences in the sequences for more than one gene
    Improve Regex searches
    Add EST functionality
    Check if the gene is too short
    Check CPG sites
    Take file input and give file output
    Find the probablilty of finding a gene based on number of conditions satisfied
    ....

    Known bugs:
    Stop Codon matching

'''


import re
import os
import mmap

                ###### Initialising parameters########
dna = input("Enter the Nucleotide Sequence () -> ").strip()
total = []
# The next two lines should be looped over and stored in a list to find all the possible codons
start = (dna.index("ATG"))
stop = dna.index("TAA")
# Ideal Example: ATACGACGGACGACGACGCAGATCCTCAGTTCTTGATACGAAAATTAGTTCTCGTAGTGTAAACAAATGTAGACTTTGAGAATTCAATTTGAATATTGGATATGTAAAGGAGTTTTGAATGATTGGATATGTGGAGTTTTGAATGATTGGATATGTATGGCGCGCAGCACTGTGCTCTGATATATCGTAACGAAAAAAAAAAAAAAAA

                ##### Checking for promoters #########
def check_for_promoters(dna):

#The file that is in the line below contains a datatbase of nucleotide sequences for promoters, by matching them with the given sequence,
# it is possible to increase the chances for finding a gene
    fn = 'output.txt'
    size = os.stat(fn).st_size
    f = open(fn)
    data = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)
    promoters = []

    while True:
        line=data.readline()
        new = line.decode('UTF-8').rstrip('\n')
        if line == b'': break
        m = re.findall(new,dna)
        if len(m) != 0:
            promoters.append(m)

    if(len(promoters) != 0):
        print("There exists at least one promoter in the given sequence")
    else:
        print("There exists no promoter that matches with the database")

                ##### Checking for TATA box #########
def check_for_TATA_box(dna):

    gap = 30
    AT_limit = 0.5
    #print(start)
    region = ''
    for i in range(-5,5):
        region += dna[start-gap+i]
        #print(start-gap+i)
    #print(region)
    if((region.count('A')+region.count('T'))/len(region) > AT_limit):
        TATA = str(start - gap)
        print("A TATA box exists around the location " + TATA + " nucleotide")

    else:
        print("A TATA box has not been found at the right location i.e 30 nucleotides downstream")

            ##### Checking for start and stop codons #########
def check_for_codons(dna):
    regex1 = r'(?=(ATG.+TAA))'
    regex2 = r'(?=(ATG.+TAG))'
    regex3 = r'(?=(ATG.+TGA))'

    one = re.findall(regex1,dna)
    two = re.findall(regex2,dna)
    three = re.findall(regex3,dna)

    total = one + two + three
    return total

            ##### Checking for GC content in the gene #########
def GC_content(total):
    GC_content = 0.5
    for i in range(0,len(total)):
        if (total[i].count("G") + total[i].count("C")) / len(total[i]) > GC_content:
            print("Possible Exons are " + total[i])

if __name__ == "__main__":
    check_for_promoters(dna)
    check_for_TATA_box(dna)
    codons = check_for_codons(dna)
    GC_content(codons)
