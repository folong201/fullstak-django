import sqlite3
from faker import Faker
import datetime
def adapt_date(date):
    return date.strftime('%Y-%m-%d')
def convert_date(date_bytes):
    return datetime.datetime.strptime(date_bytes.decode('utf-8'), '%Y-%m-%d').date()
sqlite3.register_adapter(datetime.date, adapt_date)
sqlite3.register_converter('DATE', convert_date)
conn = sqlite3.connect('ma_base_de_donnee.db')
cursor = conn.cursor()
fakeuserList = []
fake = Faker()
for _ in range(100):
    fakeuserList.append(
        (fake.first_name(), fake.email(), fake.date_this_century())                        
                        )
fakkeCommandeList = []
for _ in range(100):
    fakkeCommandeList.append(
        (fake.random_int(min=1, max=100), fake.word(), fake.random_int(min=1, max=100), fake.date_this_century())                            
                            )   
cursor.execute('''
               CREATE TABLE IF NOT EXISTS Utilisateurs(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     Nom TEXT NOT NULL,
                     Email TEXT,
                     Date_creation DATE
                )''')
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Commandes(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     ID_Utilisateur INTEGER,
                     Produit TEXT,
                        Quantite INTEGER,
                        Date_commande DATE,
                        FOREIGN KEY(ID_Utilisateur) REFERENCES Utilisateurs(ID)
                 )''')
cursor.executemany('''
               INSERT INTO Utilisateurs(Nom, Email, Date_creation)
                VALUES(?, ?, ?)
                                ''', fakeuserList)

cursor.executemany('''
                INSERT INTO Commandes(ID_Utilisateur, Produit, Quantite, Date_commande)
                 VALUES(?, ?, ?, ?)
                                  ''', fakkeCommandeList)

conn.commit()
conn.close()