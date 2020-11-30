import api.views as views
from django.urls import path, include


urlpatterns = [
    path('me/', views.UserView.as_view())
]
