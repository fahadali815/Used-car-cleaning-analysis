import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("messy_car_listings_1000.csv")

print(df.info())
print(df.describe())
print(df.duplicated().sum())
print(df.isna().sum())

df = df.drop_duplicates()


df['Listing_ID'] = df['Listing_ID'].str.strip()
df['Brand'] = df['Brand'].str.strip()
df['Model'] = df['Model'].str.strip()
df['Year'] = df['Year'].str.strip()
df['Price_AED'] = df['Price_AED'].str.strip()
df['Mileage_KM'] = df['Mileage_KM'].str.strip()
df['Fuel'] = df['Fuel'].str.strip()
df['Transmission'] = df['Transmission'].str.strip()
df['City'] = df['City'].str.strip()
df['Listing_Date'] = df['Listing_Date'].str.strip()
df['Seller_Type'] = df['Seller_Type'].str.strip()
df['Status'] = df['Status'].str.strip()

df["Model"] = df["Model"].str.replace(r'\s+', ' ', regex=True)


df['Brand'] = df['Brand'].str.title()
df['Fuel'] = df['Fuel'].str.title()
df['Transmission'] = df['Transmission'].str.title()
df['City'] = df['City'].str.title()
df['Seller_Type'] = df['Seller_Type'].str.title()
df['Status'] = df['Status'].str.title()



df['Brand'] = df['Brand'].replace({
    'Toyta': 'Toyota',
    'Hyndai': 'Hyundai',
    'Nisan': 'Nissan',
    'Mercedez-Benz': 'Mercedes-Benz'
})

df['City'] = df['City'].replace({
    'Shj': 'Sharjah',
    'Dxb': 'Dubai',
    'Abudhabi': 'Abu Dhabi'
})

df['Transmission'] = df['Transmission'].replace({
    'Auto': 'Automatic',
    'At': 'Automatic',
    'Mt': 'Manual'
})

df['Fuel'] = df['Fuel'].replace({
    'Gasoline': 'Petrol',
    'Diesal': 'Diesel'
})

df['Status'] = df['Status'].replace({
    'Avail': 'Available'
})



df['Price_AED'] = (
    df['Price_AED']
    .str.replace('AED', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

df['Mileage_KM'] = (
    df['Mileage_KM']
    .str.replace('km', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)


df['Year'] = df['Year'].replace('202O', '2020')
df['Price_AED'] = df['Price_AED'].replace('12O00', '12000')
df['Mileage_KM'] = df['Mileage_KM'].replace('85O00', '85000')


df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Price_AED'] = pd.to_numeric(df['Price_AED'], errors='coerce')
df['Mileage_KM'] = pd.to_numeric(df['Mileage_KM'], errors='coerce')



df['Listing_Date'] = pd.to_datetime(
    df['Listing_Date'],
    format='mixed',
    dayfirst=True,
    errors='coerce'
)


df.loc[~df['Year'].between(1980, 2026), 'Year'] = np.nan

df.loc[df['Price_AED'] <= 0, 'Price_AED'] = np.nan

df.loc[df['Mileage_KM'] < 0, 'Mileage_KM'] = np.nan


df['Fuel'] = df['Fuel'].replace('Water', np.nan)

df.loc[
    df['Listing_Date'] > pd.Timestamp('2026-10-04'),
    'Listing_Date'
] = pd.NaT


df = df.replace({
    'Unknown': np.nan,
    'unknown': np.nan,
    'N/A': np.nan,
    '-': np.nan,
    '': np.nan
})


df = df.dropna(subset=['Price_AED'])

df['Brand'] = df['Brand'].fillna('Unknown')
df['Model'] = df['Model'].fillna('Unknown')
df['Fuel'] = df['Fuel'].fillna('Unknown')
df['City'] = df['City'].fillna('Unknown')
df['Status'] = df['Status'].fillna('Unknown')

df[df.duplicated(subset=['Listing_ID'], keep=False)].sort_values('Listing_ID')


conflicting_listings = df[
    df.duplicated(subset=['Listing_ID'], keep=False)
].copy()

df = df[
    ~df.duplicated(subset=['Listing_ID'], keep=False)
].copy()


df['Model'] = df['Model'].replace({
    'Toyota Corolla': 'Corolla',
    'Toyota Camry': 'Camry',
    'Honda Civic': 'Civic',
    'Hyundai Tucson': 'Tucson',
    'Kia Sportage': 'Sportage',
    'Nissan Altima': 'Altima',
    'Lexus ES 300h': 'ES 300h',
    'Mercedes-Benz CLA 250': 'CLA 250'
})


outliers_review = df[
    (df['Price_AED'] > 500000) |
    (df['Mileage_KM'] > 500000)
].copy()

df = df[
    ~(
        (df['Price_AED'] > 500000) |
        (df['Mileage_KM'] > 500000)
    )
].copy()


df['Year'] = df['Year'].astype('Int64')

df = df.drop_duplicates()

df.info()


print(df.info())
print(df.describe())
print(df.duplicated().sum())
print(df.isna().sum())



df.to_csv('cleaned_car_listings.csv', index=False)


plt.figure(figsize=(10, 5))

sns.barplot(
    data=df[df['Brand'] != 'Unknown'],
    x='Price_AED',
    y='Brand',
    estimator=np.median,
    errorbar=None,
    color='steelblue'
)

plt.title('Median Listed Price by Brand')
plt.xlabel('Median Price (AED)')
plt.ylabel('Brand')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))

sns.scatterplot(
    data=df,
    x='Mileage_KM',
    y='Price_AED',
    color='steelblue',
    alpha=0.5
)

plt.title('Mileage vs Listed Price')
plt.xlabel('Mileage (km)')
plt.ylabel('Listed Price (AED)')
plt.tight_layout()
plt.show()


plt.figure(figsize=(10, 5))

sns.scatterplot(
    data=df,
    x=2026 - df['Year'],
    y='Price_AED',
    color='steelblue',
    alpha=0.5
)

plt.title('Car Age vs Listed Price')
plt.xlabel('Car Age (years, based on 2026)')
plt.ylabel('Listed Price (AED)')
plt.tight_layout()
plt.show()


