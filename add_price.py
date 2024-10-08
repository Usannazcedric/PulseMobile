import pandas as pd

def ajouter_prix_telephones(csv_path, output_csv_path):
    prix_telephones = {
        'iPhone 6 and iPhone 6 Plus': '699€',
        'iPhone 6S and iPhone 6S Plus': '749€',
        'iPhone 5S': '649€',
        'iPhone 7 and iPhone 7 Plus': '769€',
        'iPhone 11, iPhone 11 Pro and iPhone 11 Pro Max': '809€',
        'iPhone XR, iPhone XS and iPhone XS Max': '849€',
        '6600': '500€',
        '5230': '200€',
        'iPhone 5': '649€',
        'iPhone 8 and iPhone 8 Plus': '699€',
        'Galaxy S III and Galaxy S III Mini': '599€',
        'Galaxy S4': '649€',
        'iPhone X': '999€',
        'iPhone 4S': '649€',
        'Galaxy S7 and Galaxy S7 edge': '669€',
        'iPhone 4': '599€',
        'Galaxy S6 and Galaxy S6 edge': '699€',
        'N70 (N72/N73)': '400€',
        'Galaxy S8 and Galaxy S8+': '799€',
        'Galaxy S II': '649€',
        'Galaxy S10, Galaxy S10+ and Galaxy S10e': '899€',
        'Galaxy S9 and Galaxy S9+': '859€',
        'iPhone 3GS': '599€',
        'P20, P20 Pro and P20 Lite': '649€',
        'Galaxy A10': '199€',
        'Galaxy Note II': '649€',
        'Redmi Note 8 and Redmi Note 8 Pro': '200€',
        'Galaxy S20, Galaxy S20+ and Galaxy S20 Ultra': '999€',
        'Galaxy S': '599€',
        'Galaxy Grand Prime Plus': '179€',
        'Galaxy A50': '349€',
        'iPhone SE (2nd generation)': '479€',
        'Galaxy A51': '379€',
        'Galaxy A20': '219€',
        'Redmi Note 7 and Redmi Note 7 Pro': '250€',
        'P30 and P30 Pro': '899€',
        'Galaxy A21s': '199€',
        'Mate 10 and Mate 10 Pro': '699€',
        'Mate 20 and Mate 20 Pro': '899€',
        'Galaxy A01': '149€',
        'Thunderbolt': '249€',
        'Mate 9': '599€',
        'Galaxy A11': '179€',
        'Galaxy J2 Core': '99€',
        '5800 XpressMusic': '299€',
        'E71': '350€',
        'BlackBerry Pearl': '249€',
        'Redmi Note 9 Pro': '270€',
        'Galaxy S21, Galaxy S21+ and Galaxy S21 Ultra': '849€',
        'Droid Bionic': '299€',
        'Mate 30 and Mate 30 Pro': '1099€',
        'N95': '599€',
        'Galaxy Note': '699€',
        'Mi 2': '279€',
        'Galaxy Note 3': '749€',
        'G3': '549€',
        'Galaxy Note 8': '899€',
        'Redmi 6A': '99€',
        'A5': '249€',
        'Galaxy Note 9': '999€',
        'Galaxy A30': '249€',
        'Redmi 8A': '129€',
        'F1 Plus': '300€',
        'Redmi 8': '150€',
        'Galaxy J4+': '169€',
        'iPhone': '499€',
        'Galaxy J6+': '179€',
        'Galaxy Note 4': '769€',
        'Galaxy A10s': '169€',
        'Galaxy A30s': '219€',
        'N-Gage': '300€',
        'G2': '199€',
        'LeEco Le 1s': '249€',
        'Pixel and Pixel XL': '769€',
        'Centro': '199€',
        'N97': '699€'
    }

    try:
        df = pd.read_csv(csv_path)
        
        df['price'] = df['model'].map(prix_telephones)
        
        df.to_csv(output_csv_path, index=False)
        print(f"Le fichier avec les prix a été créé sous '{output_csv_path}'.")
    
    except FileNotFoundError:
        print(f"Le fichier '{csv_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue: {e}")

csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv'        
output_csv_path = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv' 

ajouter_prix_telephones(csv_path, output_csv_path)
