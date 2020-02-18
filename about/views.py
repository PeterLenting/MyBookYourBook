from django.shortcuts import render


def about_view(request):
    """Return the about.html file"""
    return render(request,  'about.html')
