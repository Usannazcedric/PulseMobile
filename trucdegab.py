import pandas as pd
 
# Creating a DataFrame with the provided data
data = {
    "No": [1, 2, 3, 4, 5, 6, 7],
    "Phone": [
        "iPhone 12 and iPhone 12 Mini",
        "Galaxy S20, S20+, S20 Ultra",
        "iPhone SE 2nd generation",
        "Galaxy A21s",
        "iPhone 12 Pro Max",
        "Galaxy A11",
        "Redmi Note 9 Pro"
    ],
    "Company": ["Apple", "Samsung", "Apple", "Samsung", "Apple", "Samsung", "Xiaomi"],
    "Sold(million)": [38, 28, 24.2, 19.4, 16.8, 15.3, 15],
}
 
# Creating a DataFrame from the data
phones_df = pd.DataFrame(data)
 
# Adding characteristics
characteristics = {
    "Screen Size (inches)": [6.1, 6.2, 4.7, 6.5, 6.7, 6.4, 6.67],
    "Camera Quality (MP)": [12, 64, 12, 48, 12, 13, 48],
    "Battery Capacity (mAh)": [2815, 4500, 1821, 5000, 3687, 5000, 5020]
}
 
# Adding the characteristics to the DataFrame
for key, value in characteristics.items():
    phones_df[key] = value
 
# Saving the updated DataFrame to a new CSV file
csv_path = '/Users/drikce/Desktop/PulseMobile/caca.csv'
phones_df.to_csv(csv_path, index=False)
 
csv_path