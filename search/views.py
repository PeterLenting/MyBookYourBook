from django.shortcuts import render
from posts.models import Post
from django.db.models import Q #for multiple searches


# Create your views here.
def do_search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(Q(author__icontains=query) | Q(title__icontains=query) | Q(condition_of_book__icontains=query) | Q(location__icontains=query)) 
    return render(request, "posts.html", {"posts": posts})
