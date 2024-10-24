import requests
import matplotlib.pyplot as plt
import datetime

COINGECKO_API_URL = "https://api.coingecko.com/api/v3"


def get_crypto_price(crypto_symbol):
    headers = {"accept": "application/json"}
    response = requests.get(f"{COINGECKO_API_URL}/simple/price", params={
        'ids': crypto_symbol,
        'vs_currencies': 'usd',
        'include_24hr_change': 'true'
    }, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if crypto_symbol in data:
            price = data[crypto_symbol]['usd']
            change_percentage = data[crypto_symbol]['usd_24h_change']
            return price, change_percentage
        else:
            raise ValueError(f"Cryptocurrency '{crypto_symbol}' not found.")
    else:
        raise Exception(f"Failed to fetch data: {response.status_code} - {response.reason}")


def get_historical_data(crypto_symbol, days):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{crypto_symbol}/market_chart", params={
        'vs_currency': 'usd',
        'days': days
    })

    if response.status_code == 200:
        data = response.json()
        if 'prices' in data:
            return data['prices']  # Returns price data over the days
        else:
            raise ValueError(f"No historical data available for '{crypto_symbol}'.")
    else:
        raise Exception(f"Failed to fetch historical data: {response.status_code} - {response.reason}")


def plot_historical_data(historical_data, crypto_symbol):
    dates = [datetime.datetime.fromtimestamp(item[0] / 1000) for item in historical_data]
    prices = [item[1] for item in historical_data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, prices, marker='o', linestyle='-', color='b')
    plt.title(f'Historical Price Data for {crypto_symbol.capitalize()}')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def main():
    crypto = input("Enter cryptocurrency symbol (eg. bitcoin, ethereum): ").lower()

    try:
        # Get real-time price and 24-hour change
        price, change = get_crypto_price(crypto)
        print(f"Current price of {crypto}: ${price}")
        print(f"24-hour change: {change:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
        return
    except Exception as e:
        print(f"Error fetching price data: {e}")
        return

    # Validate and get historical data
    while True:
        try:
            days = int(input("Enter the number of days for historical data (eg. 1, 7, 30): "))
            if days <= 0:
                raise ValueError("The number of days must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

    try:
        historical_data = get_historical_data(crypto, days)
        print("Historical data retrieved successfully.")
        plot_historical_data(historical_data, crypto)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error fetching historical data: {e}")


if __name__ == "__main__":
    main()
