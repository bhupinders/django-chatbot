import requests

from .replies.places import *
from .replies.greetings import *
from .replies.notUnderstood import *

def processQuestion(ques):
	url = 'https://api.wit.ai/message?q='
	acc = 'NY67UX2FBXSSHYPHV3FEDZPWXRIVWRL2'
	r = requests.get(url+ques+'&access_token='+acc)
	data = r.json();
	try :
		intent = data['entities']['intent'][0]['value']
		confidence = data['entities']['intent'][0]['confidence']
	except :
		intent = ''
		confidence = 0;

	print(intent, confidence)
	if confidence>0.8:
		answer = processIntent(intent, data)
	else :
		answer = nu_reply()
	return answer

def processIntent(intent, data):
	possibles = globals().copy()
	possibles.update(locals())
	method = possibles.get(intent)
	answer = method(data)
	return answer
