class Voiture:
    def __init__(self):
        self.nom = "mon de la voiture"
    def affichelenom(self):
        print(f"Le nom de la voiture est : {self.nom}")
        
ma_voiture = Voiture()
print(ma_voiture.nom)
ma_voiture.affichelenom()
