from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
    
def post_list(request):
    all_posts = Post.objects.all()                                           
    paginator = Paginator(all_posts, 3)  # Show 3 posts per page
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)
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
def post_slug_date_detail(request, year, month, day, slug, status):
    post1 = get_object_or_404(Post, 
                              status=Post.Status.PUBLISHED,
                              slug=slug, 
                              publish__year=year, 
                              publish__month=month, 
                              publish__day=day)
    return render(
        request, 'blog/post/detail.html', {'post': post1}
        )