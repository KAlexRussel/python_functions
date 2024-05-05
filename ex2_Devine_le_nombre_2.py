from random import randint
def devinette():
    print("Ceci est un jeu de devinette. Vous avez seulement 3 chances pour deviner le nombre")
    choix = input("Voulez vous jouer:(y/n):")
    if choix =="y":
        nrandom_number = randint(1, 100)
        devin_num = 101
        number_chance = 0

        while devin_num != nrandom_number:
            if number_chance == 3:
                print("nombre de chance épuisé")
                print("Game Terminated")
                break        
            devin_num = int(input("Deviner le nombre:"))
            if devin_num < nrandom_number:
                print("Trop petit")
            elif devin_num > nrandom_number:
                print("Trop Grand")                  
            else:
                print("Exact")
            number_chance = number_chance + 1

    else:
        print("Game Terminated")

   

devinette()