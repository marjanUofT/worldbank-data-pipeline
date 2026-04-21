import pandas as pd
import requests
import matplotlib.pyplot as plt


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


def plot_data(df):
    df = df.sort_values("date")
    plt.plot(df["date"], df["value"])
    plt.title("GDP per capita trend")
    plt.xticks(rotation=45)
    plt.show()

def main():
    df = fetch_data()
    df = clean_data(df)
    print(df.head())

if __name__ == "__main__":
    main()
