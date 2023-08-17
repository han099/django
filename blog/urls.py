from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="posts"),

    path('post/create',views.create_post,name="post-create"),
    path('post/edit/<int:id>', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>', views.delete_post, name='post-delete'),

    path('about/',views.about,name="about"),
    path('web01/',views.web01,name="web01"),
    path('web02/',views.web02,name="web02"),
    path('web03/',views.web03,name="web03"),
]
