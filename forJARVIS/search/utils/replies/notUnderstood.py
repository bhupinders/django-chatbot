from random import randint

replies = ["I couldn't understand what are you are saying", "Went over my head, Can you ask again?", "Sorry, but couldn't understand you at all!!", "What?", "Are you trying to test me?"]

def nu_reply():
    number = randint(0,len(replies)-1)
    return replies[number]
