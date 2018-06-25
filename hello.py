import dash
import dash_core_components as dcc
import dash_html_components as html

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from collections import *
import os
import json
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import numpy as np
from dash.dependencies import Input, Output

hello = dash.Dash()

# Twitter API log in
twit_username = "realDonaldTrump"
ckey = 'xxx'
csecret = 'xxx'
atoken = 'xxx'
asecret = 'xxx'


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
api = tweepy.API(auth)
stop_words = set(stopwords.words("english"))
newStopWords = ('RT','@', '.', ',', '!', '?', '...', '/', "'",'https', '&', '#', 'amp', ';', ':','\'','\"', '(', ')','`', '')
stop_words.update(newStopWords)

#Getting user input twitter handle, returns a <class 'tweepy.models.ResultSet'>
def tweet_list(twitname):
	tweet_list = api.user_timeline(twitname, count=300, tweet_mode="extended")
	return tweet_list

#Removes some stopwords from each tweet. Takes in the tweepy result set, and returns a counter object
def run_scrape(tweet_list):	
	total_words = Counter()
	c = Counter() #initialize coutner object
	for tweet in tweet_list: #For each tweet specified in set up of tweet_list
		if not tweet.retweeted and ('RT @' not in tweet.full_text): #if tweet ID has not been saved, and tweet is not a RT		
			words = word_tokenize(tweet.full_text) #Turns everything into tokenized words (WORD),(POS)
			filtered_sentence = []
			for w in words: 
				if w not in stop_words:
					filtered_sentence.append(w) #create new sentence with stopwords removed
			c = Counter(filtered_sentence) #creates counter object from new sentence
			total_words = Counter(c) + total_words #running total counter object	
	return total_words


#Takes in a counter object, organizes the data for use with typical graphing (MatPlotLib, Dash)
def plot_stuff(counterObj):
	x_list = []
	y_list = []
	list_30_common = (list(Counter(counterObj).most_common(30)))
	for i in range(0,len(list_30_common)):
		x = list_30_common[i][0]
		x_list.append(x)
		y = list_30_common[i][1]
		y_list.append(y)
	x_len = list(np.arange(len(x_list)))
	x_range = list(range(len(x_list)))
	return x_list, y_list, x_len, x_range

#Layout stuff
hello.layout = html.Div(children=[
	html.H1(children='Most frequently tweeted words for: '),

	html.Div(children='''
		Twitter username:
	'''),

	dcc.Input(id = 'input', value = 'realDonaldTrump', type = 'text'),
	html.Div(id='output-graph')

])


@hello.callback(
	Output(component_id='output-graph', component_property='children'),
	[Input(component_id='input', component_property='value')]
	)
def update_graph(input_Data):
	graph_title = '@' + input_Data
	tweet_list1 = tweet_list(input_Data)
	counterObj = (run_scrape(tweet_list1))
	X, Y, x_len, x_range = plot_stuff(counterObj)
	x_range = list(X)
	y_list = list(Y)
	return dcc.Graph(
		id="Graph1",
		figure={
		'data': [

		{'x': x_range, 'y': y_list, 'type': 'bar', 'name': graph_title },
		],
		'layout': {
		'title': graph_title
		}
		}
		)
	


if __name__ == '__main__':
	hello.run_server(debug=True)
