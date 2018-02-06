#!/usr/bin/python

complement = {
    'A' : 'T',
    'C' : 'G',
    'G' : 'C',
    'T' : 'A',
}

complement['A']

def reverse_complement(dna):
    list = [ complement[nucleo] for nucleo in dna]
    list = reversed(list)

    return "".join(list)

dna = "ACACGATCGGGACTTACG"
print("dna=",dna)

rc = reverse_complement(dna)
print("rc= ",rc)
