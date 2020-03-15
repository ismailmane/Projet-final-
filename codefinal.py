import nltk
import numpy as np
import re
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 

# with open('stopwordsEnglish.txt') as words_list:
# 	stop_words = words_list.read().split('\n')
# 	stop_words_set = set(stop_words)

# with open('500film.txt') as text:
# 	nb_text = len(open('500film.txt').readlines())
# 	dico = dict()
# 	for i in text.readlines():
# 		line = i.split('\t') #line[O]=ID line[1]=texte
# 		mots = set(line[1].lower().split(' '))
# 		mots = mots.difference(stop_words_set)
# 		matrix = np.array(mots)
# 		mot, cpt = np.unique(matrix, return_counts=True)
# 		dico[pid] = dict(zip(mot, cpt))
# 	print(dico)

# import re
# import math
# import numpy as np

"""
G_dico[id] = Dico[mot] -> occurence
"""
#nltk.download()
with open('stopwordsEnglish.txt') as words_list:
	vocabulaire = set()
	ps = PorterStemmer() 
	stop_words = words_list.read().split('\n') #Récuperer liste des stop words
	with open('resumetext.txt') as text:

		tampon = []
		nb_text = len(open('resumetext.txt').readlines()) # On determine le nombre de textes dans le fichier
		if (nb_text==0): 
			print('Erreur il ya 0 resume')
			quit()
		dico = dict()
		cpt = 1
		for i in text.readlines(): # On itère sur les lignes 
			i = i.strip('\n') # Pour retirer le '\n' du fichier 500 films 
			line = i.split('\t') #line[O]=ID line[1]=texte
			words = word_tokenize(line[1])# construis une chaine de caractere composée des racines de chaque mots
			racine = [ ps.stem(m) for m in words ] #  construis une liste de chaine de caractere avec les racines 
			x = " "
			text_racine = x.join(racine).lower().split(' ')
			#On recrée une string à partir de racine pour ensuite appliquer lower (met tout en minuscule) et split par rapport aux espaces

			vocabulaire.update(set(text_racine))

			matrix = np.array([text_racine]) # Création d'une matrice du texte
			tampon.append(matrix)
			pid = line[0] # Récuperation de l'ID du texte
			dico[cpt] = matrix #Inutile 
			mot, count = np.unique(matrix, return_counts=True) #Fonction pour compter les occurences des mots dans le texte
			dico[cpt] = dict(zip(mot, count))#compte les occurences de chaque mot 
			cpt+=1

		
		vocabulaire.difference_update(set(stop_words))
		#Calcul des frequences
		frequence = [] 
		for k,v in dico.items(): #Frequence parcours le premier dico
			tab = []
			ismo = dict() #on cree ismo, qui est un dictionnaire
			for mot,occ in list(v.items()):# on parcourt le deuxieme dico 
				if mot in stop_words: # Si le mot est dans stop_words on le supprime
					del dico[k][mot] #del = delete
			size = len(v)# nb de mot different 
			for mot,occ in list(v.items()):
			# formule de la ponderation 
				if nb_text> occ:
					ismo[mot] = ((occ/size)*np.log(nb_text/occ))
			#	tab.append((occ/size)*np.log(nb_text/occ))
				else: 
					ismo[mot]=0

			#frequence.append(tab)
			frequence.append(ismo)
		#print(frequence)
	with open('resumetext.txt') as text:
		### Remplissage de la matrice A 
		matrix_A = np.zeros((len(vocabulaire),nb_text),dtype = int)
		for i in range(len(vocabulaire)):
			for cpt,j in enumerate(tampon,start = 0):
				if list(vocabulaire)[i] in j:
					print('ca passe')
					matrix_A[i][cpt-1] = 1
				else:
					print('ca passe pas ')
					matrix_A[i][cpt-1] = 0
		print(matrix_A.view())

				#La remplir en virifiant si le mot est dans le texj
