"""
    Notre restaurant est fermé à cause de la crise du covid, commandez en ligne
    Dans cet exercice, vous allez écrire le code pour l'application mobile de votre restaurant afin de permettre aux clients de commander en ligne.

    Vous allez d'abord définir un menu sous forme de dictionnaire. Les clés (chaines de caractères) sont les différents repas ou boissons que vous servez et les valeurs (integers ou float) sont leurs prix correspondants.
    Une fonction restaurant se chargera de demander à l'utilisateur sa commande:

    Si la commande existe dans notre menu, le programme affiche son prix et le total actuel de ses commandes, puis lui demande d'entrée une nouvelle commande.
    Si la commande n'existe pas dans notre menu, on le dit à l'utilisateur et lui demande de commander autre chose.
    Si l'utilisateur appuie Entrée sans rien commander, on lui affiche le prix total de sa commande.
"""


def restaurant():
    print("Bienvenu dans notre Restaurant")
    print("""
            menu 
            Burger: 10,
            cafe: 7,
            cheese:15,
            shawarma: 6,
            chicha: 20
          """)
    
    menu = {
        "burger": 10,
        "cafe": 7,
        "cheese":15,
        "shawarma": 6,
        "chicha": 20
    }
        
    total = 0
    while total > -1:
        choix = input("Choississez votre commande: ").lower()
        if choix in menu:
            total +=  menu[choix]
            print(f"{choix} coûte {menu[choix]}, total est {total}")

        else :
            break

    print(f"Votre total est {total}")
    
restaurant()
