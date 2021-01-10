from .views import PostDetailsView , PostListView
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('', PostListView.as_view() , name = 'all_posts'),
    path('<int:pk>/' , PostDetailsView.as_view() , name = 'post_details'),

]