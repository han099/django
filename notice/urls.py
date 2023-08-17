from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notice_web01/',views.notice_web01,name="notice_web01"),
    path('notice_web02/',views.notice_web02,name="notice_web02"),
]
