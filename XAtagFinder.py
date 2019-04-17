#!/usr/bin/python

#Permet de sortir les lignes contenant le tag XA:
# -*- coding: utf-8 -*-

fichier = r"all-sequence.sam"
fichiersortie = r"fichiersortieXA.txt"
STRING = "XA:"
 
with open(fichier,'r') as fi:
    with open(fichiersortie,'w') as fs:
        for ligne in fi:
            if STRING in ligne:
                fs.write(ligne)

