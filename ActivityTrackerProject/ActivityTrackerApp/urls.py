from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_activity/', views.newActivity, name='new_activity'),
    path('activity/<int:id>/', views.activity, name='activity'),
    path('activity/<int:id>/new_timelog/', views.newTimelog, name='new_timelog'),
]