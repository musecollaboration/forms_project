from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from .forms import FeedbackForms
from .models import Feedback
from django.views.generic import ListView

from django.views import View


class FeedbackView(View):
    def get(self, request: HttpRequest):
        form = FeedbackForms()
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request: HttpRequest):
        form = FeedbackForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        return render(request, 'feedback/feedback.html', context={'form': form})


class UpdateFeedbackView(View):
    def get(self, request: HttpRequest, id_feedback=None):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForms(instance=feed)
        return render(request, 'feedback/feedback.html', context={'form': form})

    def post(self, request: HttpRequest, id_feedback=None):
        feed = Feedback.objects.get(id=id_feedback)
        form = FeedbackForms(request.POST, instance=feed)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/done')
        form = FeedbackForms(instance=feed)
        return render(request, 'form_project/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I.'
        context['date'] = '01.01.2025'
        return context


class ListFeedBack(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedbacks'

    def get_queryset(self):
        queryset = super().get_queryset()
        # filter_qs = queryset.filter(rating__gt=2)
        return queryset


class DetailFeedBack(TemplateView):
    template_name = 'feedback/detail_feedback.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_feedback = int(kwargs['id_feedback'])
        context['one_data'] = Feedback.objects.get(id=id_feedback)
        return context
