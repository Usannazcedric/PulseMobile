import pandas as pd

# Chemin vers le fichier CSV
file_path = '/Users/drikce/Desktop/PulseMobile/mobile_sales (1).csv'

# Lire le fichier CSV dans un DataFrame
df = pd.read_csv(file_path)

# Vérifier si la colonne 'MobileModel' existe, puis la supprimer
if 'MobileModel' in df.columns:
    df = df.drop(columns=['MobileModel'])
    print("Colonne 'MobileModel' supprimée avec succès.")
else:
    print("La colonne 'MobileModel' n'existe pas dans ce fichier.")

# Enregistrer le DataFrame modifié dans un nouveau fichier CSV
df.to_csv('/Users/drikce/Desktop/PulseMobile/mobile_sales_modified.csv', index=False)

print("Fichier modifié enregistré sous 'mobile_sales_modified.csv'.")
