from django.urls import path
from . import views


urlpatterns=[
    path('', views.HomePageView.as_view(), name='home'),
    path('detail/', views.DetailListView.as_view(), name='detail'),
]

