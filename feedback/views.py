from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import FeedbackForms


def index(request: HttpRequest):

    if request.method == 'POST':
        form = FeedbackForms(request.POST)
        if form.is_valid():
            print(form.changed_data)
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForms()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request: HttpRequest):
    return render(request, 'feedback/done.html')
