from django.urls import path
from . import views
from .views import JoinFormView

urlpatterns = [
    path('join', JoinFormView.as_view()),
]
