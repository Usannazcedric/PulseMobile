import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'Phone': [
        'iPhone 12 and iPhone 12 Mini',
        'Galaxy S20, S20+, S20 Ultra',
        'iPhone SE 2nd generation',
        'Galaxy A21s',
        'iPhone 12 Pro Max',
        'Galaxy A11',
        'Redmi Note 9 Pro'
    ],
    'Company': [
        'Apple', 'Samsung', 'Apple', 'Samsung', 
        'Apple', 'Samsung', 'Xiami'
    ],
    'Sold(million)': [
        38.0, 28.0, 24.2, 19.4, 16.8, 15.3, 15.0
    ],
    'price': [
        809, 999, 479, 199, 1159, 179, 270
    ]
}

df = pd.DataFrame(data)

print("Données chargées :")
print(df)

years = [2021, 2022, 2023, 2024]
predictions = {}

for year in years:
    X = df[['price']] 
    y = df['Sold(million)']  

    model = LinearRegression()
    model.fit(X, y)

    df[f'Predicted_Sales_{year}'] = model.predict(X)
    predictions[year] = df[['Phone', 'Company', 'price', f'Predicted_Sales_{year}']]
    
    df['Sold(million)'] = df[f'Predicted_Sales_{year}'] * 1.05

for year in years:
    print(f"\nPrédictions des ventes pour {year} :")
    print(predictions[year])
