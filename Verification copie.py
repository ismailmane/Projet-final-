import nltk
import numpy as np
import re
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 



"""
G_dico[id] = Dico[mot] -> occurence
"""
#nltk.download()
with open('stopwordsEnglish.txt') as words_list:
    
    listefinal=[]
    vecteurRequete=np.array([])
    vecteurDocument1=np.array([])
    vecteurDocument2=np.array([])
    vecteurDOCSSS=np.array
    vecteurDocu=np.array([])
    Liste=[]
    listedesresumer=[]
    tupleponderation=[]
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
        DICOFINAL=dict()
        for i in text.readlines(): # On itère sur les lignes `
            
         
                
            i = i.strip('\n') # Pour retirer le '\n' du fichier 500 films 
            
            line = i.split('\t') #line[O]=ID line[1]=texte
          
            DICOFINAL[line[0]]=line[1]
            #print('la worrrrrrrrrrrrrrrdddddddddd')
            words = word_tokenize((line[1]),language='english', preserve_line=False)# construis une chaine de caractere composée des racines de chaque mots

            #print(words)
            #print('la raaaaaaaacine')
            racine = [ ps.stem(m) for m in words ] #  construis une liste de chaine de caractere avec les racines 
            #print (racine)
            x = " "
           # print('tesssssssstddddd')
            text_racine = x.join(racine).lower().split(' ')
           #10films print(text_racine)
            listedesresumer.append(text_racine)
            
           
			#On recrée une string à partir de racine pour ensuite appliquer lower (met tout en minuscule) et split par rapport aux espaces
            vocabulaire.update(set(text_racine))
           
            matrix = np.array([text_racine]) # Création d'une matrice du texte
            tampon.append(matrix)
           
            pid = line[0] # Récuperation de l'ID du texte
            pid_list.append(pid)
            dico[cpt] = matrix #Inutile 
            mot, count = np.unique(matrix, return_counts=True) #Fonction pour compter les occurences des mots dans le texte
            dico[cpt] = dict(zip(mot, count))#compte les occurences de chaque mot 
            cpt+=1
          
		
        vocabulaire.difference_update(set(stop_words))
		#Calcul des frequences
        frequence = [] 
        
        for k,v in dico.items(): #Frequence parcours le premier dico
          
          
            tab = []
            
            ismo = dict() #on cree ismo, qui est un dictionnaire$
            
      
            for mot,occ in list(v.items()):# on parcourt le deuxieme dico 
              
          
                if mot in stop_words: # Si le mot est dans stop_words on le supprime
                   
                    del dico[k][mot] #del = delete
                    
                size = len(v)# nb de mot different 
                
            for mot,occ in list(v.items()):
                
              
                if nb_text> occ:
                    
                    ismo[mot] = ((occ/size)*np.log(nb_text/occ))
                 
                if nb_text==occ:
                   
                    ismo[mot] = ((occ/size)*np.log(nb_text/occ))
                   
                else: 
                    ismo[mot]=0
                
                for elt in enumerate(list(v.items())):
                    elt= mot,((occ/size)*np.log(nb_text/occ))
                    tupleponderation.append(elt)
                  
                
      
        
        
        requete = input("Veuillez entrer une requete : ")
        
        
        
        
        requete= requete.split()
        print('Voici la requete choisis')
        print(requete)
       
        cpt=0
        tupleponderation=list(set(tupleponderation))
        #print(requete.lower())
        for i in requete:
            ps.stem(i)
          
           
           
            if i in stop_words1:
               
                del requete[cpt]
            cpt=cpt+1   
       
        listdevocabulaire=list(vocabulaire)
        print(requete)
        ide=0
        
        listdevocabulaire=list(vocabulaire)
        
        listdevocabulaire=sorted(listdevocabulaire)
        #print(listdevocabulaire)
      
        propa=[]
        pond=0
    
        compt=0
        ks=0
        testeeee=[]
        miniscule=[]
        #print(requete)
        for i in requete:
            
          
            miniscule.append(i.lower())
        
        requete=miniscule
        
    
        for i in requete:
            
            ks=0
            for j in listdevocabulaire:
                if i.lower()==j:
                    
                    testeeee.append(ks)
                    
                ks=ks+1
    
      
        testeeee=sorted(testeeee)
        
       
    
        sommee=0
       
        listdevocabulaire.sort()
     
        vecteurRequete=np.array([])
        # print('La liste de la requete')
        # print(requete)
       
       # print('Le vecteur requete ')
        chahchah=[]
        filtre=[]
        for sal,mer in tupleponderation:
            filtre.append(sal)
        
        for u,v in tupleponderation:
            for zey in filtre:
                
                if zey ==u:
               
                    
                        elts=zey,v
                        filtre.remove(zey)
                        
                        chahchah.append(elts)
                        
        ddd=0          
        listeRequzte=[]
        i=0
        for testons in listdevocabulaire:
            if testons in requete:
                for preer, ponderj in chahchah:
                    if testons==preer:
                        listeRequzte.append(ponderj)
            else:
                listeRequzte.append(0)
        #print('taille requuuuuueeeeettttteee')     
      #  print('Voici la liste requete')
        #print(listeRequzte)
        #print('chachahc')
        #print(len(chahchah))
        #print(len(listdevocabulaire))
        
        vecteurRequete=np.array(listeRequzte)
        print('La liste de requete')
        print(listeRequzte)
       # print(listeRequzte)
        print('Le vecteur requete')
        print(vecteurRequete)
        # print('')
        "tessvffffffffffffffffffffttttt"
        
        filtre=[]
        for sal,mer in tupleponderation:
            filtre.append(sal)
        "partie tessssssssssssssssttttttttt"   
       
        maybef=[]
      
    
        
        chahmat = [item for item in filtre if item not in listdevocabulaire]
     
        filtre=list(set(filtre))
     
        
        
        
        
        
        
        chah=0
        chahchah=[]
        #print('prefimbu')
        print(len(filtre))
        for u,v in tupleponderation:
            for zey in filtre:
                
                if zey ==u:
               
                    
                        elts=zey,v
                        filtre.remove(zey)
                        
                        chahchah.append(elts)
       # print('fimfimbudimvu')   
     
        #print(len(chahchah))        
        #print('jecrois jsusssssssssss')
            
     
        
        
        #print('jjsssssuuuuuiiiss chaudddddd')
        
        #print(mana)
        
        #print(len(set(tupleponderation)))
        #tuple
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        "cette partie est bonne normalement change list np"
        listetexte=[]
        for k,v in dico.items():
        
            for mottz in listdevocabulaire:
                #print(mottz)
                
                if mottz in v:
                    for perr,poonder in chahchah:
                        if mottz == perr:
                            listetexte.append(poonder)
            
                    
                else:
                    listetexte.append(0)
                    

                    
           # print(' Le vecteur document ')
            i=i+1

            vecteurDocc=np.array(listetexte)
            
            #print(vecteurDocc)
            #print('jee peeeeenssse llleeeee probeleme est la')
            #print('ponderation')
            #print(vecteurDocc)
           
            
            #print('liste vocabu')
           # # print(len(listdevocabulaire))
           # # print(listdevocabulaire)
           #  print('')
           #  print('requete')
           #  print(len(vecteurRequete))
           #  print('docu')
           # # print(len(vecteurDocc))
            #print('ERRRRRRRRRRRRRROOOOOOOOOORRRRRRR')
            resut=vecteurRequete.dot(vecteurDocc)
           # print('la finnnnnnnnnnn')
            
            
            maybef.append(resut)
         
        
            listetexte=[]
     
            ddd=ddd+1
            
            maxi=0
            sm=0
            print('La liste des resultats')
            #print(maybef)
            for bon in maybef:
                
                if bon>=maxi:
                    maxi=bon
                    sm=sm+1
                #print(sm)
                    
        if maxi>0:
                 
                #print('Voici la liste des differents resutats de la forumule cos ')   
                #print(resut)
                print("L'identifient du film le plus adéquate ")
                print(pid_list[sm-1])
            
        else:
             print('Aucun film correspond à votre requete veuillez saisir une nouvelle requete!!')
  