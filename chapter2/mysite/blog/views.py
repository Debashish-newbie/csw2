from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name ='posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

    
    
# def post_list(request):
#     all_posts = Post.objects.all()                                           
#     paginator = Paginator(all_posts, 3)  # Show 3 posts per page
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     return render(
#         request, 'blog/post/list.html', {'posts': posts}
#         )
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
    
def post_share(request, post_id):
    # get the post
    post = get_object_or_404(
        Post, 
        id=post_id, 
        status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            # create post URL
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']} comments: {cd['comments']}"
            # send email
            send_mail(
                subject,
                message,
                cd['email'],   # sender
                [cd['to']]     # receiver
            )
            
            sent = True
            
    else:
        form = EmailPostForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post,
                   'form': form,
                   'sent': sent}
                  )