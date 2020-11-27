import requests
import os
import json

def get_bearer_token():
    # Open the file 'twitter_key', return its contents.
    return open('twitter_key').read()

def create_headers():
    headers = {"Authorization": "Bearer {}".format(get_bearer_token())}
    return headers

def search_tweets(username):
    headers = create_headers()
    twitter_recents_api_url = "https://api.twitter.com/2/tweets/search/recent"
    url_with_parameters = twitter_recents_api_url + "?" + "query={}&{}".format('from:' + username, 'max_results=100')
    response = requests.request("GET", url_with_parameters, headers=headers)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def check_tweet_to_add(tweet_string):
    if tweet_string[0:4] == 'RT @':
        return False
    return True

def clean_tweets_string(tweet_string):
    return tweet_string.replace('\n', '').replace('\r', '')


def get_tweets_for_user(username):
    json_response = search_tweets(username)
    #print(json.dumps(json_response, indent=4))
    list_of_tweets = json_response['data'];
    return_string = ''

    for tweet in list_of_tweets:
        if check_tweet_to_add(tweet['text']):
            return_string += tweet['text']
    
    return clean_tweets_string(return_string)

def main():
    print(get_tweets_for_user('realDonaldTrump'))

if __name__ == "__main__":
    main()