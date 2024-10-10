import pandas as pd

def replace_smartphone_column(input_csv, output_csv):
    df = pd.read_csv(input_csv)
    
    df['smartphone'] = df['smartphone'].replace({'Yes': 'SmartPhones', 'No': 'FeaturePhones'})
    
    df.to_csv(output_csv, index=False)
    print(f"Le nouveau fichier CSV a été créé : {output_csv}")

input_csv = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv' 
output_csv = '/Users/drikce/Desktop/PulseMobile/best-selling-mobile-phones.csv' 
replace_smartphone_column(input_csv, output_csv)
