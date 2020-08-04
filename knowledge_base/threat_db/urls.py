from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('threat/<str:id>/', views.threat, name='threat_view'),
]