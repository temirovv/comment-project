from django.urls import path

from .views import CommentAPIView, PeopleAPIView


urlpatterns = [
    path('comments/', CommentAPIView.as_view()),
    path('people/', PeopleAPIView.as_view()),
]