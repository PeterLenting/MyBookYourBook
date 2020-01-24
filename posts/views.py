from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.http import HttpResponseForbidden
from django.contrib import messages


def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'posts.html' template
    """
    print("Ran")
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    for p in posts:
        print(p)
    return render(request, "posts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postdetail.html", {'post': post})


def edit_post(request, pk=None):
    """
    Create a view that allows user to edit
    his own post and a superuser to edit all posts.
    """
    post = get_object_or_404(Post, pk=pk)
    if (request.user == post.provider or
            request.user.is_superuser):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(post_detail, post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return HttpResponseForbidden()

    return render(request, 'postform.html', {'form': form})


def new_post(request, pk=None):
    """
    Create a view that allows user to add
    a new book.
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.provider = request.user
                post.save()
                return redirect('get_posts')
        else:
            form = PostForm()
    return render(request, 'postform.html', {'form': form})


def delete_post(request, pk=None):
    """
    Create a view that allows user to delete
    his own post and a superuser to delete all posts.
    """
    post_id = int(pk)
    post = get_object_or_404(Post, pk=post_id)
    if (request.user == post.provider or
            request.user.is_superuser):
        if request.method == 'POST':
            try:
                post.delete()
                messages.success(request,
                                 'You have successfully deleted your post')
            except Post.DoesNotExist:
                messages.warning(request, 'The post could not be deleted')
    else:
        return HttpResponseForbidden('You are only allowed to delete your own post')

    return redirect('get_posts')
