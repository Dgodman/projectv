from django.shortcuts import render


def index(request):
    '''Home page of site'''

    # render html
    return render(
        request,
        'vote/index.html',
        {'active_nav': 'home',},
    )


def about(request):
    '''Home page of site'''

    # render html
    return render(
        request,
        'vote/about.html',
        {'active_nav': 'about',},
    )