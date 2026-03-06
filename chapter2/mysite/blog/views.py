from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404

def post_list(request):
    posts = Post.objects.all()
    return render(
        request, 'blog/post/list.html', {'posts': posts}
        )
def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No post found')
    return render(
        request, 'blog/post/detail.html', {'post': post}
        )
def post_slug_date_detail(request, year, month, day, slug, Status):
    post1 = get_object_or_404(Post, 
                              status=Post.Status.PUBLISHED,
                              slug=slug, 
                              publish__year=year, 
                              publish__month=month, 
                              publish__day=day)
    return render(
        request, 'blog/post/detail.html', {'post': post1}
        )