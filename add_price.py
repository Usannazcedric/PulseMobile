import pandas as pd

def ajouter_prix_telephones(csv_path, output_csv_path):

    prix_telephones = {
        'iPhone 12 and iPhone 12 Mini': '€809',
        'Galaxy S20, S20+, S20 Ultra': '€999',
        'iPhone SE 2nd generation': '€479',
        'Galaxy A21s': '€199',
        'iPhone 12 Pro Max': '€1,159',
        'Galaxy A11': '€179',
        'Redmi Note 9 Pro': '€270'
    }

    try:
        df = pd.read_csv(csv_path)
        
        prix_list = []
        
        for model in df['Phone']:
            found_price = None
            for key in prix_telephones:
                if key in model:  
                    found_price = prix_telephones[key]
                    break
            prix_list.append(found_price if found_price else 'N/A')
        
        df['price'] = prix_list
        
        df.to_csv(output_csv_path, index=False)
        print(f"Le fichier avec les prix a été créé sous '{output_csv_path}'.")
    
    except FileNotFoundError:
        print(f"Le fichier '{csv_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

csv_path = '/Users/drikce/Desktop/PulseMobile/Best Selling Mobile Phones 2020.csv'         
output_csv_path = '/Users/drikce/Desktop/PulseMobile/Best Selling Mobile Phones 2020.csv' 

ajouter_prix_telephones(csv_path, output_csv_path)
