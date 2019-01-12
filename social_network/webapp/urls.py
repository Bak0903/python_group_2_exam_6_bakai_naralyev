from django.urls import path
from webapp.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, delete_post


app_name = 'webapp'

urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),
    path('post/create', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post_update'),

    path('post/<int:post_id>/delete', delete_post, name='post_delete'),

]