import pandas as pd

def supprimer_lignes_sans_smartphone(csv_path, output_csv_path):
    try:
        df = pd.read_csv(csv_path)
        
        if 'smartphone' in df.columns:
            df_filtered = df[df['smartphone'] == 'Yes']
            
            df_filtered.to_csv(output_csv_path, index=False)
            print(f"Les lignes avec 'No' dans la colonne 'smartphone' ont été supprimées.")
            print(f"Le fichier filtré a été enregistré sous '{output_csv_path}'.")
        else:
            print("La colonne 'smartphone' n'existe pas dans ce fichier.")
    
    except FileNotFoundError:
        print(f"Le fichier '{csv_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")


csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv'
output_csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv' 

supprimer_lignes_sans_smartphone(csv_path, output_csv_path)
