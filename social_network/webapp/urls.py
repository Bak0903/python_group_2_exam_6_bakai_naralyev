from django.urls import path
from webapp.views import PostListView


app_name = 'webapp'

urlpatterns = [
    path('post_list/', PostListView.as_view(), name='post_list'),

]