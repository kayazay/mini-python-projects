# External Libraries installed are:
# tweepy
# pilow (PIL)

import auth_file as af
import requests
import tweepy
from json import loads
from datetime import datetime as dt
from PIL import Image
from sys import exit

def btc_crawler():
    url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': af.pro_api_key,
    }
    params = {
        'symbol':'BTC',
    }
    # make request to CoinMarketCap API
    try:
        res =  requests.get(url, params=params, headers=headers)
        data = loads(res.text)
        # streamline HTML output to get only what we need
        shortened = data.get('data').get('BTC')[0].get('quote').get('USD')
        # get price and time information
        price = round(shortened.get('price'),2)
        str_timestamp = shortened.get('last_updated')
        # get elements of timestamp
        _timestamp = dt.strptime(str_timestamp, "%Y-%m-%dT%H:%M:%S.000Z")
        full_date = _timestamp.date().strftime('%B %d, %Y')
        full_time = _timestamp.time().strftime("%I:%M%p")
        # output_text to be tweeted
        output_text = f'It is {full_date} at {full_time} UTC...\nDo you own any #BTC?\nQuestions? DM @DoubleSalesClub\n\nCurrent price:\n${price:,.2f} (via CoinMarketCap)'
        return output_text
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def TweetIt():
    # get image from url
    img_url = 'https://svbtleusercontent.com/3r8bHQsSTfr7t7vam88Snk0xspap.png'
    res = requests.get(img_url, stream=True)
    if not res.status_code == 200:
        exit('Image not found')
    print('Render image from url')
    img = Image.open(res.raw)
    img.thumbnail((600,600))
    img.save('picture.png')
    # input Twitter API keys
    auth = tweepy.OAuthHandler(
        af.consumer_key, # consumer key goes here
        af.consumer_secret # consumer secret goes here
    )
    auth.set_access_token(
        af.access_token, # access token goes here
        af.access_secret # access token secret goes here
    )
    print('Connect to Twitter API')
    api = tweepy.API(auth)
    # upload image from url
    print('Upload image')
    media = api.media_upload('picture.png')
    print('Get BTC price from site')
    tweet = btc_crawler()
    if tweet:
        print('Make the actual tweet')
        #print(tweet)
        status = api.update_status(status=tweet, media_ids= [media.media_id]
        )
        print('Successfully tweeted')
    else:
        return 'Issue from CoinMarketCap API'


if __name__ == '__main__':
    TweetIt()
