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
	stop_words=words_list.read().split('\n')#Récuperer liste des stop words
	with open('500film.txt') as text:


		nb_text = len(open('500film.txt').readlines()) # On determine le nombre de textes dans le fichier
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
			
			pid = line[0] # Récuperation de l'ID du texte
			dico[cpt] = matrix #Inutile 
			mot, cpt = np.unique(matrix, return_counts=True) #Fonction pour compter les occurences des mots dans le texte
			dico[cpt] = dict(zip(mot, cpt))#compte les occurences de chaque mot 
			cpt+=1

		vocabulaire.difference_update(set(stop_words))
		#Calcul des frequences
		frequence = [] 
		for k,v in dico.items(): #Frequence parcours le premier dico
			tab = []
			dico1 = dict() #on cree grand dico , qui est un dictionnaire
			for mot,occ in list(v.items()):# on parcourt le deuxieme dico 
				if mot in stop_words: # Si le mot est dans stop_words on le supprime
					del dico[k][mot] #del = delete
			size = len(v)# nb de mot different 
			for mot,occ in list(v.items()):
			# formule de la ponderation 
				dico1[mot] = ((occ/size)*np.log(nb_text/occ))
			#	tab.append((occ/size)*np.log(nb_text/occ))
			#frequence.append(tab)
			frequence.append(dico1)
		print(max(frequence[1]))

		### Remplissage de la matrice A 
		matrix_A = np.zeros((len(vocabulaire),nb_text),dtype = int)
		print(matrix_A)
		for i in range(len(vocabulaire)):
			for j in range(nb_text):
				#La remplir en virifiant si le mot est dans le text
