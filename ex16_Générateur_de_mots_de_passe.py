"""
    Nous allons écrire une fonction generateur_password qui nous génère des mots de passe. 
    Cette fonction est un peu particulière car elle retournera une autre fonction password. 
    Certains sites n'acceptent que les mots de passe qu'avec des lettres, ou qu'avec des chiffres, ou acceptent des symboles comme @/$ ou simplement un mélange de tout ceci.

    La fonction generateur_password prend en entrée une chaine de caractères contenant les différents caractères possible et retourne la fonction password que je peux éxécuter plus tard en lui donnant le nombre de caractères que je veux dans mon mot de passe.

    Exemple:

    password = generateur_password('Aer5-/')
    mon_password = password(7)
    print(mon_password)
    > 'eA-Ae5/'

"""

from random import choice

def generateur_password(st):
    def password(num):
        sd = list(st)
        new=""
        for _ in range(num):
            f = choice(sd)
            new= new + f

        return new

    return password

password = generateur_password('Aer5-/')
mon_password = password(2)
print(mon_password)


    

