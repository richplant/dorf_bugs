import config
import tweepy
import csv
from random import randint
import itertools
import os

def pick_text():
	with open(os.path.join(os.getcwd(),'gen_texts.csv'), encoding='utf-8') as f:
		texts = list(csv.reader(f))
		n = randint(0, len(texts))
		return texts[n][0]

def main():
	auth = tweepy.OAuthHandler(config.api_key, config.api_key_secret)
	auth.set_access_token(config.access_token, config.access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
	text = pick_text().strip("'").strip('"')
	api.update_status(status=text)

if __name__ == '__main__':
	main()