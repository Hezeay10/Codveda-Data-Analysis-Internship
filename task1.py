import pandas as pd

df = pd.read_csv("3) Sentiment dataset.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.isnull().sum())
print("Number of duplicate rows:")
print(df.duplicated().sum())
df = df.drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)
print(df.columns)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Date'] = df['Timestamp'].dt.date
df['Time'] = df['Timestamp'].dt.time
df = df.drop('Timestamp', axis=1)
df = df.drop('Year', axis=1)
df = df.drop('Month', axis=1)
df = df.drop('Day', axis=1)
text_columns = ['Sentiment', 'Platform', 'Country', 'User', 'Hashtags']

for column in text_columns:
    df[column] = df[column].str.strip().str.title()
print(df.info())
df.to_csv("cleaned_sentiment_dataset.csv", index=False)
print("Cleaning completed successfully!")