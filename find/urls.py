from django.urls import path

from . import views

urlpatterns = [

path('', views.find.as_view()),
path('id', views.ajax_find_id_view),
path('pw_find', views.RecoveryPwView.as_view(), name='recovery_pw'),
path('pw_find/find/', views.ajax_find_pw_view, name='ajax_pw'),
path('pw_find/auth/', views.auth_confirm_view, name='recovery_auth'),

]