class Voiture:
    roues = 4
    moteur = 1
    def __init__(self) :
        self.nom = "A determiner"

    
class Voiture_sport(Voiture):
    def __init__(self):
        self.nom = "FERRARI"
        
voiture = Voiture_sport()

print("voiture.moteur ") 
voiture.roues = 5
print(voiture.roues) # 5
print(voiture.nom)

class Temperature:
    def __init__(self, temperature, unit="C"):
        self.temperature = temperature
        self.unit = unit

    def to_fahrenheit(self):
        if self.unit == "F":
            return self.temperature
        return (self.temperature * 1.8) + 32

    def to_celsius(self):
        if self.unit == "C":
            return self.temperature
        return (self.temperature - 32) / 1.8

unit = input("Entrez la l'unite de la temperature(C pour celcius et F pour fahrenheit): ")
tempe = int(float(input("Entrez la temperature: ")))
temp = Temperature(tempe, unit)
print(temp.temperature)
print(temp.unit) 
print(temp.to_fahrenheit()) 
print(temp.to_celsius())  
