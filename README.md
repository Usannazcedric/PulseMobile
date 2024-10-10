# PulseMobile

### README for Python Scripts

---

#### **PREDICTOR2000.py**

**Description**:  
This script uses machine learning to predict future smartphone sales based on historical data stored in a CSV file. It leverages a linear regression model to forecast phone sales by taking into account phone prices from previous years and making predictions for subsequent years.

**Features**:
- Reads a CSV file with columns for the phone model, company, sales in millions, and price.
- Trains a linear regression model to predict sales for the following year.
- Predicts sales for multiple consecutive years (up to 2024) by using the predictive sales of previous years.

**Usage**:
- Ensure the CSV file is structured with the following columns: `Phone`, `Company`, `Sold(million)`, and `price`.
- Run the script to see the sales forecasts printed in the console.

**Command**:  
```bash
python3 PREDICTOR2000.py
```

---

#### **add_price.py**

**Description**:  
This script adds a new column to a CSV file containing phone prices. It's useful for completing a CSV file with missing price information for phones.

**Features**:
- Adds a `price` column to the CSV with phone prices.

**Usage**:  
Edit the source CSV file and run the script to automatically add the price column.

**Command**:  
```bash
python3 add_price.py
```

---

#### **change_no_and_yes.py**

**Description**:  
This script modifies specific cell values in a CSV file, replacing `no` with `FeaturePhones` and `yes` with `SmartPhones`.

**Features**:
- Changes cells with "no" to "FeaturePhones".
- Changes cells with "yes" to "SmartPhones".

**Usage**:  
This script is helpful for standardizing values in your CSV documents.

**Command**:  
```bash
python3 change_no_and_yes.py
```

---

#### **remove_columns.py**

**Description**:  
This script removes unnecessary columns from a CSV file, making it more readable or relevant for analysis.

**Features**:
- Removes one or more specified columns from a CSV file.

**Usage**:  
Edit the source CSV and specify which columns you wish to remove.

**Command**:  
```bash
python3 remove_columns.py
```

---

#### **remove_les_pas_smartphones.py**

**Description**:  
This script removes rows from a CSV file where the phones are not smartphones, based on the classification in the data (e.g., "FeaturePhones").

**Features**:
- Deletes all rows where the phones are not smartphones (e.g., "FeaturePhones").

**Usage**:  
Ideal for filtering data and keeping only smartphones in the CSV file.

**Command**:  
```bash
python3 remove_les_pas_smartphones.py
```

---

#### **trucdegab.py**

**Description**:  
This script generates a CSV file based on specific data requested by a collaborator. It extracts and organizes the relevant information in a structured format.

**Features**:
- Creates a new CSV file from specific data points.

**Usage**:  
Use this script to respond to specific data requests from collaborators by organizing the information into a new CSV file.

**Command**:  
```bash
python3 trucdegab.py
```

---

### General Notes:
- Ensure Python 3.x is installed.
- Install the necessary dependencies using:
  ```bash
  pip install pandas scikit-learn numpy
  ```
- Check the file paths of the CSV files before running each script.
