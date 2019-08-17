from django.urls import path
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    #path('', views.home, name="blog-home"),
    path('',PostListView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('user/<username>/',UserPostListView.as_view(),name='user-posts'),
    path('post/new/',PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update',PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='post-delete'), #Needs a template post_confirm_delete.html
    path('about/', views.about, name="blog-about"),
]
