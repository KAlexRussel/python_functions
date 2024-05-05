'''  
    Ecris une fonction nommée devinette qui ne prend aucun argument.
    Quand on l'exécute, elle choisit un nombre aléatoire en 0 et 100 (inclus)et demande à l'utilisateur de deviner ce nombre.A chaque fois que l'utilisateur entre un nombre, le programme affiche l'une de ces phrases :

    Trop grand
    Trop petit
    Exact
    Si l'utilisateur a choisit correctement, le programme s'arrete. 
    Sinon, le programme demande encore à l'utilisateur de rentrer un nouveau nombre jusqu'à ce qu'il trouve la bonne solution et s'arrête.

 '''
from random import randint
def devinette():
    nrandom_number = randint(1, 100)
    devin_num = 101
    while devin_num != nrandom_number:

        devin_num = int(input("Deviner le nombre:"))

        if devin_num < nrandom_number:
            print("Trop petit")
        elif devin_num > nrandom_number:
            print("Trop Grand")                  
        else:
            print("Exact")

devinette()
