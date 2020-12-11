import api.views as views
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenVerifyView,
    TokenRefreshView
)

urlpatterns = [
    path('token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/',
         TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
    path('organizations/<uuid:orgId>/contacts/',
         views.ContactsView.as_view(), name='contacts'),
    path('organizations/<uuid:orgId>/contacts/<uuid:contactId>/',
         views.ContactView.as_view(), name='contact'),
    path('organizations/<uuid:orgId>/contacts/<uuid:contactId>/notes/',
         views.ContactNoteView.as_view(), name='contact_notes'),
    path('organizations/<uuid:orgId>/members/',
         views.MembersView.as_view(), name='members'),
    path('organizations/<uuid:orgId>/members/<uuid:memberId>/',
         views.MemberView.as_view(), name='member'),
    path('organizations/<uuid:orgId>/requests/',
         views.RequestsView.as_view(), name='requests'),
    path('organizations/<uuid:orgId>/requests/<uuid:requestId>/',
         views.RequestView.as_view(), name='request'),
    path('users/',
         views.UsersView.as_view(), name='users'),
    path('users/<uuid:userId>/',
         views.UserView.as_view(), name='user'),
    path('users/<uuid:userId>/notifications/',
         views.NotificationsView.as_view(), name='notifications'),
    path('users/<uuid:userId>/notifications/<uuid:notificationId>/',
         views.NotificationView.as_view(), name='notification')
]
