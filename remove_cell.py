import pandas as pd

file_path = '/Users/drikce/Desktop/PulseMobile/mobile_sales (1).csv'

df = pd.read_csv(file_path)

if 'MobileModel' in df.columns:
    df = df.drop(columns=['MobileModel'])
    print("Colonne 'MobileModel' supprimée avec succès.")
else:
    print("La colonne 'MobileModel' n'existe pas dans ce fichier.")

df.to_csv('/Users/drikce/Desktop/PulseMobile/mobile_sales_modified.csv', index=False)

print("Fichier modifié enregistré sous 'mobile_sales_modified.csv'.")
