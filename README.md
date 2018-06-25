# TwitWords
Continuation of Trump Tweets in a way. It has been modified to be presented via Flask/Dash web application.
Takes user input for Twitter Handle and returns a graph of the user's most frequently used words.
<br>
<br>
Required Libraries:<br>
dash<br>
dash_core_components as dcc<br>
dash_html_components as html<br>
tweepy<br>
tweepy import Stream<br>
tweepy import OAuthHandler<br>
collections import *<br>
os<br>
json<br>
nltk.tokenize import sent_tokenize, word_tokenize<br>
nltk.corpus import stopwords<br>
numpy as np<br>
dash.dependencies import Input, Output<br>
  
Known bugs:
Input has not been sanitized properly yet to prevent unwanted strings from being passed to the graph. (ex: 'https', '"', 'www')
