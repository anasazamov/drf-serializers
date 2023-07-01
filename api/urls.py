from django.urls import path
from .views import TaskView


urlpatterns = [
    path('task/', TaskView.as_view()),
    path('task/<int:pk>/', TaskView.as_view()),
]