
from django.urls import path
from members.views import Show_members , Member_Detail
urlpatterns = [

    path('members/', Show_members, name='members'),
    path('members/detail/<int:id>/', Member_Detail, name='detail')
]