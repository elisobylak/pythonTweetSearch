# coding=utf-8
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os, ConfigParser, tweepy, inspect

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# read in config file
config = ConfigParser.SafeConfigParser()
config.read(os.path.join(path, "config"))

# create bot with auth keys
auth = tweepy.OAuthHandler(config.get("twitter", "consumer_key"), config.get("twitter", "consumer_secret"))
auth.set_access_token(config.get("twitter", "access_token"), config.get("twitter", "access_token_secret"))
api = tweepy.API(auth)

# search query goes in-side the quotes
results = api.search(q = '#shoesh')

for result in results:
    print result.text
