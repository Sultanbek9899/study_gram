from django.urls import path

from apps.post.views import get_posts, test_post

urlpatterns = [
    path('', get_posts, name='get_posts'),
    path('test/', test_post, name='post_test')
]