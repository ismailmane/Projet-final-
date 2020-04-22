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
    amad=0
    listefinal=[]
    vecteurDocument1=np.array([])
    vecteurDocument2=np.array([])
    vecteurRequete=np.array([1])
    vecteurDocu=np.array([])
    Liste=[]
    at=0
    cpt=0
    cttt=0
    vocabulaire = set()
    ps = PorterStemmer() 
    stop_words1 = words_list.read() #Récuperer liste des stop words
    stop_words=stop_words1.split('\n')
    filename = input("Veuillez entrer un nom de fichier : ")
    try:
        f = open(filename, "r")
    except:
            print("Le fichier", filename, "est introuvable")
 
    
    with open(filename) as text:
    
        tampon = []
        nb_text = len(open(filename).readlines()) # On determine le nombre de textes dans le fichier
        if (nb_text==0): 
            print('Erreur il ya 0 resume')
            quit()
        dico = dict()
        cpt = 1
        pid_list=[]
        
        for i in text.readlines(): # On itère sur les lignes `
            
            # # print(i)
            
            # if manal in i:
            #     # print('monchah')
                
                
            # else:
            #     print("cest la merde")
                
            i = i.strip('\n') # Pour retirer le '\n' du fichier 500 films 
            
            line = i.split('\t') #line[O]=ID line[1]=texte
            
            words = word_tokenize((line[1]),language='english', preserve_line=False)# construis une chaine de caractere composée des racines de chaque mots

            # print(words)
            
            racine = [ ps.stem(m) for m in words ] #  construis une liste de chaine de caractere avec les racines 
            # print(racine)
            x = " "
            # print(x)
            text_racine = x.join(racine).lower().split(' ')
            # print('jsuis la')
           
            # print('jsuis pas la')
			#On recrée une string à partir de racine pour ensuite appliquer lower (met tout en minuscule) et split par rapport aux espaces
            vocabulaire.update(set(text_racine))
            # print(vocabulaire.update(set(text_racine)))
            # print('chelsea')
            matrix = np.array([text_racine]) # Création d'une matrice du texte
            tampon.append(matrix)
            #tampon.view(matrix)
        
            # print(type(matrix))
            # print(type(tampon))
            # print(tampon)
            # print('natalie')
            pid = line[0] # Récuperation de l'ID du texte
            pid_list.append(pid)
            dico[cpt] = matrix #Inutile 
            mot, count = np.unique(matrix, return_counts=True) #Fonction pour compter les occurences des mots dans le texte
            dico[cpt] = dict(zip(mot, count))#compte les occurences de chaque mot 
            cpt+=1
           # print(matrix)
           # print(type(matrix['23890098']))
            #print(matrix['23890098'])
		
        vocabulaire.difference_update(set(stop_words))
		#Calcul des frequences
        frequence = [] 
        
        for k,v in dico.items(): #Frequence parcours le premier dico
          
            # print(dico.items())
            tab = []
            # print(k)
            # print('buuuug11111')
            # print(type(k))
            # print(type(v))
            ismo = dict() #on cree ismo, qui est un dictionnaire$
            
      
            for mot,occ in list(v.items()):# on parcourt le deuxieme dico 
              
                #print(list(v.items()))
                 # print(str(mot))
                 # print(type(occ))
                #print('mamamazey')
                 # print(mot)
                 # print('azerttyy')
              
                # print('premier boucleeeeeee')
                
                # print(occ)
                # print('femmmmme')
                
               
                #print(mot)
                #print(occ)
                if mot in stop_words: # Si le mot est dans stop_words on le supprime
                    # print(mot)
                    
                    # print('ya un bail ')
                    # print(mot)
                    # print(dico[k][mot])
                    del dico[k][mot] #del = delete
                    
                size = len(v)# nb de mot different 
                
            for mot,occ in list(v.items()):
                # print('boucleeeeeee2222')
                # print('chahchah')
                # print(mot,occ)
                
            
 			# formule de la ponderation 
                # print('zeeeeeeynab')
                # print( nb_text)
                # print('dffggggggggggggg')
              
                if nb_text> occ:
                    ismo[mot] = ((occ/size)*np.log(nb_text/occ))
                    # print('mamamamamndddd')
                    # print(ismo[mot])
                    # print('occurence petite')
                    # print(mot)
                if nb_text==occ:
                    # print('sa mere la pu')
                    print('nbtext=occ')
 			#	tab.append((occ/size)*np.log(nb_text/occ))
                else: 
                    ismo[mot]=0
                    # print(mot)
                    # print('zeerrrrrrrrrrooooooooo')
   
        
        requete = input("Veuillez entrer un mot : ")
        tol=input("Veuillez entrer une tol : ")
    #     for mot, occ in list(v.items()):
    #         print(mot)
    #         print(list(v.items()))
            
    #         print('jsuis bien cuittttttt')
    #         print(manal)
    #         print(str(mot))
    #         if ps.stem(manal) == str(mot):
                
    #             print(mot)
    #             print('jsuis trop chaud')
    #             print(cpt)
    #             cpt=cpt+1
 
           
    #         else:
    #             print('totalement cuit')
    #             print('va dormir ')
                
          
    #         if ps.stem(zeynab )== str(mot ):
    #             print('jsuis trop chaud')
    #             cttt=cttt+1
    #             print(cttt)
            
    #         else:
    #             print('va dormir ')
 			# #frequence.append(tab)
        frequence.append(ismo)
       
   
    for ko,v in dico.items():
        
    
        if (requete in v):
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            print(pid_list)
            amad=amad+1
            print('nombrer')
            print(amad)
            
            nb= v[requete]
        
            for aze in range(0,len(v)):
                vecteurRequete=np.append(vecteurRequete,0)
                #print('je confirme jsuis chaud')
                if aze<=nb:
                    vecteurDocument1=np.append(vecteurDocument1,1)
                    #print('meme plus')
                else:
                    vecteurDocument2=np.append(vecteurDocument2,0)
                    #print('ohohlalalala')
            vecteurDocu=np.append(vecteurDocument1,vecteurDocument2)
       
            frere= np.transpose(vecteurRequete)
            
            normeRequete=np.linalg.norm(vecteurRequete)
            normeDocu=np.linalg.norm(vecteurDocu)
           
            while(len(vecteurDocu)!=len(vecteurRequete)):
                if (len(vecteurDocu)<len(vecteurRequete)):
                    
                    vecteurDocu=np.append(vecteurDocu,0)
                
                else:
                    vecteurRequete=np.append(vecteurRequete,0)
            
            if (np.dot((vecteurRequete),(vecteurDocu)))> float(tol):
            
       
                Liste.append(k)
          
                listefinal =listefinal.append(cpt)
                print(vecteurRequete)
                print(vecteurDocu)
                print(vecteurDocument1)
                print(vecteurDocument2)
                
            #Liste.append(k)
        vecteurDocument1=np.array([])
        vecteurDocument2=np.array([])
        vecteurRequete=np.array([1])
        vecteurDocu=np.array([])
    print(Liste ) 
    print(vecteurRequete)
    print(vecteurDocu)
    print(vecteurDocument1)
    print(vecteurDocument2)
    print(listefinal)
  
    print(pid_list[amad-1])
    
  
        # print(list(v.items()))
        # print('puuuute')
        # print(ismo)
           
        # print(vocabulaire)
        
    
#     print(at)
# #         filename1 = input("Veuillez entrer un mot1 : ")
        
# #         try:
# #             print(filename1)
# #             ps.stem(filename1)
# #             print(ps.stem(filename1))
# #         except:
# #             print("Le fichier", filename, "est introuvable")
            
# #         filename2=input("Veuillez entrer un mot2 :")
# #         try:
# #             print(filename2)
# #             ps.stem(filename2)
# #             print(ps.stem(filename2))
# #         except:
            
# #             print("Le fichier", filename, "est introuvable")
# #         L=[]
        
        
#         # print(lower(vocabulaire.update(set(text_racine))))
        
#         for k,v in dico.items():
            
#             print(v)
#             if filename1 in v:
#                 print('azerrtttt')
#             else:
#                 print('putain')
#             for mot,occ in list(v.items()):

#                 if str(mot)==filename1:
#                     print('aaaaaaaa')
#                     L.append(k)
#                     print(L)  
#                     print("teste1")
                    
#                 # if filename2 in vocabulaire:
#                 #     print('bbbbbbb')
#                 #     L.append(k)
#                 #     print(L)
#                 #     print("teste2")
                    
    
        
# #     with open(filename) as text:
# # 		### Remplissage de la matrice A 
# #             matrix_A = np.zeros((len(vocabulaire),nb_text),dtype = int)
# #             for i in range(len(vocabulaire)):
# #                 for cpt,j in enumerate(tampon,start = 0):
# #                     if list(vocabulaire)[i] in j:
# #                         print('ca passe')
# #                         matrix_A[i][cpt-1] = 1
# #                     else:
# #                             print('ca passe pas ')
# #                             matrix_A[i][cpt-1] = 0
# #             print(matrix_A.view())
# #             print('fin3')
# # 				#La remplir en virifiant si le mot est dans le texj

