from django.shortcuts import render

# Create your views here.
from apps.post.models import Post


def get_posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def test_post(request):
    context = {
        "title": "This is my test post",
        "random_number": 124124,
    }
    return render(
        request,
        'post_test.html',
        context=context
  )
