from django.views.generic.base import TemplateView
from .forms import FeedbackForms
from .models import Feedback
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView


class FeedbackView(CreateView):
    model = Feedback
    form_class = FeedbackForms
    # fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class UpdateFeedbackView(UpdateView):
    model = Feedback
    form_class = FeedbackForms
    # fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'


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


class DetailFeedBack(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback  # в html будет в нижнем регистре feedback или object
    # context_object_name = 'feed'  # переопределение переменной
