class CarteBancaire:
    def __init__(self, proprietaire, solde):
        self.proprietaire = proprietaire
        self.solde = solde


class CompteEpargne(CarteBancaire):
    def __init__(self, proprietaire, solde, taux_interet):
        super().__init__(proprietaire, solde)
        self.__taux_interet = taux_interet

    def modifier_taux_interet(self, nouveau_taux):
        self.__taux_interet = nouveau_taux

    def get_taux_interet(self):
        return self.__taux_interet


compte1 = CompteEpargne("alise", 1000, 1.05)
print(compte1.get_taux_interet())  
compte1.__taux_interet=5    # cette affectetion echoue car __taux_interet n'est pas un attribu public
print(compte1.get_taux_interet()) 
compte1.modifier_taux_interet(12)  # affectation passe car on utilise un setter
print(compte1.get_taux_interet())   

class Employer:
    def __init__(self,nom,salaire,annee) :
        self.nom = nom
        self.annee = annee
        self.salaire = salaire
    
    
class Manager(Employer):
    def  __init__(self, nom, salaire, annee):
        super().__init__(nom, salaire, annee)
        # self.performance =performane
        
    def augmenter_salaire(self,performance =80):
        self.performance = performance
        if performance>80:
            prim = min(performance*100,10000)
            self.salaire +=prim
            print(f"Augmentation salariale : {prim}")
            print(f"Votre nouveaux salaire est de : {self.salaire}")
        
class Annimal:
    def __init__(self,nom):
        self.nom = nom
        
        
class AnnimalMarin(Annimal):
    def __init__(self, nom,catergorie):
        super().__init__(nom)
        self.categorie = catergorie
    def estMamifere(self):
        if self.categorie == "mamifere":
            print("Cet annimal est un manifere")
        else :
            print("Cet n'est pas annimal est un manifere")
            