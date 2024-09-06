class Rectagle:
    def __init__(self,long,larg) :
        self.long = long
        self.larg = larg
    def calcule_perimetre(self):
        result = 2*(self.long+self.larg)
        print(f"Le perimetre est: {result}")
        
        
rect = Rectagle(10,8)
rect.calcule_perimetre()

class Etudiant:
    def __init__(self,nom,age,note):
        self.nom = nom
        self.age = age
        self.note=note
    def afficher_resultat(self):
        if self.note>=10:
            print(f"etudiants{self.nom} est admis")
        else:
            print(f"Etudiant {self.nom} a echouer")
            
            
            
etudiant = Etudiant("Folong",22,13)
etudiant.afficher_resultat()