
from django.urls import path , include
from members.views import Show_members
urlpatterns = [
    
    path('members/',Show_members.as_view(),name='members'),
]