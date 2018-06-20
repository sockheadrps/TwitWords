# TwitWords
Continuation of Trump Tweets in a way. It has been modified to be presented via Flask/Dash web application.
Takes user input for Twitter Handle and returns a graph of the user's most frequently used words.

Required Libraries:
  dash
  dash_core_components as dcc
  dash_html_components as html
  tweepy
  tweepy import Stream
  tweepy import OAuthHandler
  collections import *
  os
  json
  nltk.tokenize import sent_tokenize, word_tokenize
  nltk.corpus import stopwords
  numpy as np
  dash.dependencies import Input, Output
  
  Known bugs:
  Input has not been sanitized properly yet to prevent unwanted strings from being passed to the graph. (ex: 'https', '"', 'www')
