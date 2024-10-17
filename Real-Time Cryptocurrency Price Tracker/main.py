import requests

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
        price = data[crypto_symbol]['usd']
        change_percentage = data[crypto_symbol]['usd_24h_change']
        return price, change_percentage
    else:
        return None


def get_historical_data(crypto_symbol, days):
    response = requests.get(f"{COINGECKO_API_URL}/coins/{crypto_symbol}/market_chart", params={
        'vs_currency': 'usd',
        'days': days
    })
    if response.status_code == 200:
        return response.json()['prices']  # Returns price data over the days
    else:
        return None


def main():
    print("You may refer to https://api.coingecko.com/api/v3/coins/list for the coins list")
    crypto = input("Enter cryptocurrency symbol (e.g. bitcoin, ethereum): ").lower()
    price, change = get_crypto_price(crypto)

    if price:
        print(f"Current price of {crypto}: ${price}")
        print(f"24-hour change: {change:.2f}%")

        # Get historical data
        days = input("Enter the number of days for historical data: ")
        historical_data = get_historical_data(crypto, days)
        if historical_data:
            print(historical_data)
            print("Historical data retrieved successfully.")
            # You may process historical_data further (e.g., plot or analyze it)
    else:
        print("Invalid cryptocurrency symbol or failed API request.")


if __name__ == "__main__":
    main()
