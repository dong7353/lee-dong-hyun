from django.urls import path
from mypage import views

urlpatterns = [
    path('', views.mypage),
    # path('/calendar/', views.mypagecalendar),
]

