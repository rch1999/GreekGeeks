import api.views as views
from django.urls import path, include


urlpatterns = [
    path('users/', views.UsersView.as_view()),
    path('users/<uuid:uuid>/', views.SpecificUsersView.as_view())
]
