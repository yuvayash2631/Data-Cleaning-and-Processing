import pandas as pd


df = pd.read_csv('Customer_Personality_Analysis.csv')

print(df.head())

print(df.isnull().sum())
df.dropna(inplace=True)
df['Income'].fillna(df['Income'].median(), inplace=True)

print(df.duplicated().sum())


df.drop_duplicates(inplace=True)
df['Gender'] = df['Gender'].str.lower().str.strip()  # convert to lowercase and remove spaces
df['Gender'] = df['Gender'].replace({'m': 'male', 'f': 'female'})
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
df.columns = df.columns.str.lower().str.strip().str.replace(' ', '_')

df['age'] = 2025 - df['year_birth']
df['age'] = df['age'].astype(int)
df.to_csv('cleaned_dataset.csv', index=False)
