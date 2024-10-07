import pandas as pd
import random

capitales = [
    "Paris", "London", "Berlin", "Madrid", "Rome", "Ottawa", "Tokyo", "Washington", "Brasilia", 
    "Beijing", "Canberra", "New Delhi", "Moscow", "Pretoria", "Buenos Aires"
]




file_path = '/Users/drikce/Desktop/PulseMobile/mobile_sales_modified.csv'

df = pd.read_csv(file_path)

if 'Location' in df.columns:
    df['Location'] = df['Location'].apply(lambda x: random.choice(capitales))
    print("La colonne 'Location' a été mise à jour avec des capitales au hasard.")
else:
    print("La colonne 'Location' n'existe pas dans ce fichier.")

df.to_csv('/Users/drikce/Desktop/PulseMobile/mobile_sales_with_random_capitals.csv', index=False)

print("Fichier modifié enregistré sous 'mobile_sales_with_random_capitals.csv'.")
