from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeedbackView.as_view()),
    path('done', views.DoneView.as_view()),
    path('list', views.ListFeedBack.as_view()),
    path('detail/<int:pk>', views.DetailFeedBack.as_view()),  # pk или slug
    path('update/<int:pk>', views.UpdateFeedbackView.as_view()),  # pk или slug
    path('<int:id_feedback>', views.UpdateFeedbackView.as_view()),

]
