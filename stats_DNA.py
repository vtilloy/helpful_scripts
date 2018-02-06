#!/usr/bin/python

nbA = nbC = nbG = nbT = nbTotal = 0

dna = "TATCCTTATGACTGGACGACGCAAT"

print(dna)

for nucleotide in dna:
    if nucleotide == 'A':
        nbA += 1
    elif nucleotide == 'C':
        nbC += 1
    elif nucleotide == 'G':
        nbG += 1
    elif nucleotide == 'T':
        nbT += 1
    nbTotal += 1

print("sequence length", nbTotal)
print("A = ", 100*nbA/nbTotal)
print("C = ", 100*nbC/nbTotal)
print("G = ", 100*nbG/nbTotal)
print("T = ", 100*nbT/nbTotal)

