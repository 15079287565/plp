from django.conf.urls import url
from django.urls import path

from stu import views

urlpatterns = [
    path('', views.index_view),

    path('login/', views.login_view),
    path('show/', views.shwo_view),
    path('reg/', views.reg_view),
    path('mov/', views.mov_view),



]

