from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('activity/',views.activity, name='activity'),
    path('group/',views.group, name='group'),
    path('usercreation/', views.usercreation, name = 'usercreation'),
    path('profile/', views.profile, name = 'profile'),
    path('viewthread/', views.viewthread, name = 'viewthread'),
    path('userview/',views.userview,name="userview"),
]

