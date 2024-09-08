from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    trending = Post.objects.get(trending=True)
    posts = Post.objects.filter(trending=False)
    return render(request, 'blogapp/index.html', {'trending': trending, 'posts': posts})

def readmore(request, slug):
    post = Post.objects.get(slug = slug)
    comments = post.comment_set.all()
    form = CommentForm()
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        new_comment = form.save(commit = False)
        new_comment.post = post
        new_comment.save()
        return HttpResponseRedirect(reverse('readmore', kwargs={'slug': slug}))
    return render(request, 'blogapp/readmore.html', {'post': post, 'comments': comments, 'form': form})
