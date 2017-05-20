#-*- coding: latin-1 -*

def maj_affichage(c, mot_affiche, mot_mystere):
	if type(c) != str or type(mot_affiche) != str or type(mot_affiche) != str:
		raise TypeError("plz use strings")
	elif len(c) > 1:
		raise ValueError("plz use a single character")

	i = 0
	mot_affiche = list(mot_affiche)	#conversion en liste pour manipuler plus facilement (affectations)
	while i < len(mot_mystere):
		print("i=",i)
		if mot_mystere[i] == c:
			mot_affiche[i] = c
		i+=1
	mot_affiche = "".join(mot_affiche)
			
	return mot_affiche

if __name__ == "__main__":
	"""test u"""
	print(maj_affichage('a', "****", "caca"))
	print(maj_affichage('b', "****", "caca"))
	while True:
		a=0