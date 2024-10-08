import pandas as pd

def supprimer_colonne(csv_path, column_name, output_csv_path):
    try:
        df = pd.read_csv(csv_path)
        
        if column_name in df.columns:
            df = df.drop(columns=[column_name])
            print(f"La colonne '{column_name}' a été supprimée.")
            
            df.to_csv(output_csv_path, index=False)
            print(f"Le fichier modifié a été enregistré sous '{output_csv_path}'.")
        else:
            print(f"La colonne '{column_name}' n'existe pas dans ce fichier.")
    
    except FileNotFoundError:
        print(f"Le fichier '{csv_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv'        
column_name = 'form'             
output_csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv' 

supprimer_colonne(csv_path, column_name, output_csv_path)
