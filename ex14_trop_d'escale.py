"""
    Vous êtes dans une agence de voyage pour acheter un billet d'avion. 
    Vous donnez la destination à l'agent qui vous informe, qu'il faudra faire des escales. 
    Il vous dit alors la ville de chaque escale et la duree de chaque escale. 
    Vous décidez d'enregistrer tout cela dans un dictionnaire pour l'afficher plus tard et la somme des heures d'escales.

    Vous allez écrire un programme qui demande à l'agent la ville (clé) et le nombre d'heure d'escale (valeur). 
    Le programme lui repose la même question jusqu'à ce qu'il dit que c'est fini en appuyant entrée sans rien écrire. A la fin de la saisie, vous affichez les villes et leur nombre d'heures correspondant et le nombre d'heures total d'escale.

    Exemple:

    Python Airlines

    Ville: Paris, nb d'heures : 2
    Ville: Nairobi, nb d'heures : 1
    Ville: Bamako, nb d'heures : 0.5
    Ville: Abuja, nb d'heures : 2.5
    Ville: <entréee>

"""

def escale():

    destination = {
        "paris": 2,
        "nairobi": 1,
        "bamako":0.5,
        "abuja": 2.5
    }
        
    total = 0
    list_escal=[]
    while total > -1:
        choix = input("Choississez votre destination: ").lower()
        if choix in destination:
            total +=  destination[choix]
            list_e =f"{choix} {destination[choix]}"
            list_escal.append(list_e)

        else :
            break

    print("Liste des escales :")
    for lis in list_escal:
        print(lis)
    print(f"Votre total d'heures d'escales est {total} heures")
    
escale()