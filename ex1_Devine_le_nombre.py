'''   '''
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
