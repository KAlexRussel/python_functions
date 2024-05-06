"""
    Dans cet exercice, vous allez écrire une fonction wordcount qui prend en entrée le chemin d'un fichier et affiche les 4 lignes suivantes en sortie:

    Le nombre de caractères (les espaces inclus) est ....
    Le nombre de mots (séparé par des espaces: 25 est un mot) est .....
    Le nombre de lignes est ....
    Le nombre de mots distincts ("Oui" et "oui" sont 2 mots uniques) est .... (taille du vocabulaire du fichier)
    Un fichier texte nommée count.txt se trouve dans le dossier datasets. Vous pouvez l'utiliser pour tester votre cod
"""


def wordcount(filename):
    f = open(filename, "r")
    count = 0;   
    ligne = []
    char =[]
    x=[]   

    for line in f:
        ligne.append(line)
        #Splits each line into words  
        words = line.split(" ")
        print(words)  
        #Counts each word  
        count = count + len(words)
        
        for word in words:
            if word not in x:
                x.append(word)
                print(word)


        for l in line:
            char.append(l)

    print(f"Le nombre de caractères est: {len(char)} ")
    print(f"Le nombre de mots est: {count}")
    print(f"Le nombre de lignes est: {len(ligne)} ") 
    print(f"Le nombre de mots distincts est:{len(x)}") 

    f.close();  


wordcount(r'C:\Users\DELL\Desktop\communication\count.txt')