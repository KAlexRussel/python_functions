"""
    Créez une classe Vehicule avec les attributs suivants:

    couleur
    distance_parcourue (km)
    vitesse maximum (km/h)
    vitesse actuelle (km/h)
    On peut donc créer un nouveau véhicule ce cette manière :

    v1 = Vehicule(couleur='bleu', vitesse_maximum='100')
    Ajoutez à la classe Vehicule les méthodes ou fonctionalités suivantes:

    accelerer : augmente la vitesse actuelle sur une durée(minutes) sans dépasser la vitesse maximum
    ralentir : diminue la vitesse sur une durée (minutes)
    arreter : elle met à 0 la vitesse actuelle
    la fonction _repr_ qui permet d'afficher le nombre de distance parcourue et l'état (arrêt, en cours) quand on fait print(v1)
"""

class Vehicule:
    def __init__(self,couleur,distance_parcourue, vitesse_max,vitesse_actuelle):
        self.couleur = couleur
        self.distance_parcourue = distance_parcourue
        self.vitesse_max = vitesse_max
        self.vitesse_actuelle =vitesse_actuelle

    def accelerer(self, durer):
        a = self.vitesse_actuelle + durer
        if a > self.vitesse_max:
            self.vitesse_actuelle = self.vitesse_max
        else:
            self.vitesse_actuelle = a 

    def ralentir(self, durer):
        self.vitesse_actuelle = self.vitesse_actuelle - durer

    def arreter(self):
        self.vitesse_actuelle = 0

    def __repr__(self):
        if self.vitesse_actuelle == 0:
            d = "arrêt"
        else:
            d ="en cours"
        return f"La distance parcourue est de: {self.distance_parcourue } km et l'etat: {d} "
    

makween = Vehicule(couleur='bleu', vitesse_max=100, vitesse_actuelle=23, distance_parcourue=23)

print(f"le vehicule est de couleur {makween.couleur} ")
print(f"la vetisse actuelle est de: {makween.vitesse_actuelle} km/h")
makween.arreter()
print(f"le vehicule accelere a: {makween.vitesse_actuelle} km/h")

print(makween)

    


        
