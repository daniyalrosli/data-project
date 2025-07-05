import pandas as pd
from sqlalchemy import create_engine

# Load data from CSV
df = pd.read_csv('../data/air_quality_sample.csv')  # Update path as needed
print('Data loaded:')
print(df.head())

# Connect to SQLite database (or change to your DB)
engine = create_engine('sqlite:///../data/air_quality.db')

# Write data to SQL table
df.to_sql('air_quality', engine, if_exists='replace', index=False)
print('Data written to SQL database.')

# Query data from SQL
df_sql = pd.read_sql('SELECT * FROM air_quality LIMIT 5', engine)
print('Queried data:')
print(df_sql) 




 