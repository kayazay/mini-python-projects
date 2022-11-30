# BTC CRAWLER

## This is a simple, dockerized web crawler application made with Python.

<img src = "https://user-images.githubusercontent.com/60517587/204914487-9482816c-c497-48c9-8509-5f1822a7ebf3.gif" width=60% height=20% />

And yes, this is infact my first time containerizing with Docker 😃 

+ This app makes a request to **`CoinMarketCap`**- a reliable source of information for Crypto-currency prices.

+ Extracts relevant data from API endpoints and processes this into a tweet.

+ Downloads image from url to be used along with tweet.

+ Esablishes connection with Twitter API and makes the tweet.

**NOTE:** API keys and link to image were saved into variables in a different Python script- **auth_file** and then called in main script.

## External Python Libraries used:

+ **PIL**- to work with images easily;

+ **Tweepy**- to access Twitter API.

## How to Run This App Locally

+ Spin up your terminal and run a `git clone` to clone this repo

+ `cd` to the **btc-twitter-app** directory

+ Create a python script- **auth_file.py** to hold API keys.

+ Run a `docker build -t preferred-name-of-image` to build the Dockerfile into an image.

+ `docker run preferred-name-of-image` to start up the container

+ Logging messsages would be printed and tweet made successfully.

---

<p>&copy; 2022 Kingsley Izima</p>
