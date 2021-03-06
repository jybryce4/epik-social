from django.urls import include, path
from . import views
from .views import (
    PostListView, PostDetailView, 
    PostCreateView, PostUpdateView,
    PostDeleteView, UserPostListView,
)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('user/profile/<str:username>/', views.get_user_profile, name="public-profile"), 
    path('post/<int:pk>/likes/', views.like_post, name='likes'), # doesn't work yet
]
