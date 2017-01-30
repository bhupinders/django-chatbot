from random import randint

replies = ["Ha ha ha", "blah blah blah", "What??", "Gone Mad?", "Ya, sure"]

def greetings(data):
    number = randint(0,len(replies)-1)
    return replies[number]
