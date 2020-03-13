from django.shortcuts import render


def rent_view(request):
    """Return the rent.html file"""
    return render(request,  'rent.html')
