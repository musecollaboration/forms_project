from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'feedback/feedback.html')


def hello(request):
    print(request.GET['name'])
    print(request.GET['surname'])
    return HttpResponseRedirect('/')
    # return render(request, 'feedback/feedback.html')
