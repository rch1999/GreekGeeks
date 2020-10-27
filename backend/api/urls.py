from api.views import UserView
from django.urls import path, include


urlpatterns = [
    path('me/', UserView.as_view()),
]