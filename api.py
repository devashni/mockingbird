import requests
import os
import json

def auth():
    return 'secret key' #move to secrets.sh


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def search_tweets(headers):
    username = 'realDonaldTrump'
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format('from:' + username, 'max_results=100')
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    bearer_token = auth()
    headers = create_headers(bearer_token)
    json_response = search_tweets(headers)
    print(json.dumps(json_response, indent=4))
    tweets = json_response["data"]
    for tweet in tweets:
        print(tweet['text'])


if __name__ == "__main__":
    main()