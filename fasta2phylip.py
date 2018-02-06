#! /usr/bin/python

with open('dna.fasta.py', 'r') as f, open('dna.phylip.py', 'w') as file_out:
    for line in f:
        line = line.strip()
        print(line)
        if line[0] == '>':
             file_out.write('{}\t'.format(line.strip('>')))
        else:
             file_out.write('{}\n'.format(line))