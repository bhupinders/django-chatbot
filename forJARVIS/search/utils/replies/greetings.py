from random import randint

replies = ["Hi, What you doing?", "Hi, How can I help You", "Hi!!", "Hi, nice to meet you!", "Hello!"]

def greetings(data):
    number = randint(0,len(replies)-1)
    return replies[number]
