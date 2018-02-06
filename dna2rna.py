#!/usr/bin/python

def translate_dna_to_rna(dna):
    rna = ""
    for nucleo in dna:
        if nucleo == 'T':
            rna += "U"
        else:
            rna += nucleo
    return rna
    
dna = "ATTCCGGGTATTACG"
print(dna)
rna = translate_dna_to_rna(dna)
print(rna)
