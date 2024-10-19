# Cryptocurrency Price Tracker with CoinGecko API

## Project Overview

The **Real-Time Cryptocurrency Price Tracker** is a Python script that allows users to retrieve real-time cryptocurrency prices, percentage price changes, and historical price data using the CoinGecko public API. The script also offers a simple visualization of historical price trends. Refer to [CoinGecko API](https://docs.coingecko.com/v3.0.1/reference/introduction) and [CoinGecko Coins List](https://api.coingecko.com/api/v3/coins/list) for more information.

## Features

- **Real-Time Price Retrieval**: Input the name of a cryptocurrency (eg. bitcoin) to retrieve its current price in USD
- **24-Hour Price Change**: Displays the 24-hour percentage change in price for the selected cryptocurrency
- **Historical Price Data**: Retrieve historical price data for a specified number of days (eg. 1 day, 7 days, or 30 days) and visualize it in a chart
- **Data Visualization**: Uses matplotlib to generate a line chart displaying the historical price data


## Technologies Used

- **Python**: The core programming language used to build the script
- **CoinGecko API**: A free API used to fetch cryptocurrency prices, percentage changes, and historical data
- **Requests**: A Python library for making HTTP requests to the CoinGecko API
- **Matplotlib**: A Python library used to visualize historical cryptocurrency price data in a line chart format
- **Datetime**: Python datetime module is used to convert and handle timestamps when retrieving historical price data

## Prerequisites

Before running the application, ensure you have the following:

- [Python 3.x](https://www.python.org/downloads/) installed on your system
- `requests` and `matplotlib` libraries are installed. Refer to `requirements.txt` for a specific version
  
