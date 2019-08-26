from django.shortcuts import render

def index(request):
    context = {
        'title': 'User'
    }
    return render(request, 'login.html', context)

