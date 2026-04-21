import pandas as pd
import requests

def fetch_data():
    url = "http://api.worldbank.org/v2/country/USA;CAN/indicator/NY.GDP.PCAP.CD?format=json"
    response = requests.get(url)
    data = response.json()[1]
    df = pd.DataFrame(data)
    return df

def clean_data(df):
    df = df[['country', 'date', 'value']]
    df = df.dropna()
    return df

def main():
    df = fetch_data()
    df = clean_data(df)
    print(df.head())

if __name__ == "__main__":
    main()
