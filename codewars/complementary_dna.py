r"""
Complementary DNA

Instructions

Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.

If you want to know more: http://en.wikipedia.org/wiki/DNA

In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". Your function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input --> output)

"ATTGC" --> "TAACG"
"GTAT" --> "CATA"
"""

def DNA_strand(dna: str) -> str:
    for i in range(len(dna)):
        if dna[i] == 'A':
            dna = dna[:i] + 'T' + dna[i+1:]
        elif dna[i] == 'T':
            dna = dna[:i] + 'A' + dna[i+1:]
        elif dna[i] == 'C':
            dna = dna[:i] + 'G' + dna[i+1:]
        elif dna[i] == 'G':
            dna = dna[:i] + 'C' + dna[i+1:]
    return dna

def main():
    print(DNA_strand("AAAA"),"TTTT")
    print(DNA_strand("ATTGC"),"TAACG")
    print(DNA_strand("GTAT"),"CATA")

if __name__ == "__main__":
    main()