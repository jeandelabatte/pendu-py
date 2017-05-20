#-*- coding: latin-1 -*
import os
import random as rand
import donnees
from fonctions import *

coups=donnees.max_coups
score=		TO BE CONTINUED
points=
ind_mot_mystere = rand.randint(0, len(donnees.mots)-1)
mot_mystere = donnees.mots[ind_mot_mystere]
mot_affiche=[]
for c in mot_mystere:
	mot_affiche.append('-')
mot_affiche="".join(mot_affiche)

print("Bienvenue dans ce jeu de pendu")

while coups > 0:
	print("Il vous reste ", coups, " tentatives pour trouver le mot mystère")
	print(mot_affiche)
	while not ok
		try:
			c=input("Proposez une lettre : ")
		except ValueError:
			print("Veuillez entrer un caractère")
		else:
			ok=True
	maj_affichage(c, mot_affiche, mot_mystere)
	if mot_affiche == mot_mystere:
		print("C'est gagné ! Votre score est de ", score)

os.system("pause")
