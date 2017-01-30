from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from .forms import MyForm
from utils.intent import processQuestion

# Create your views here.
def index(request):
    questions = []
    q1 = ('Ask something human!!')
    questions.append(q1)
    return render(request,'search/home.html',{'questions':questions})

def get_question(request):
    questions = []
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = MyForm(request.POST)
        question = (request.POST['question'])
        questions.append(question)

        answer = processQuestion(question)
        questions.append(answer)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = MyForm()

    return render(request, 'search/home.html', {'questions': questions})
