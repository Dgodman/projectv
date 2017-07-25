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
    '''About of site'''

    # render html
    return render(
        request,
        'vote/about.html',
        {'active_nav': 'about',},
    )


def start(request):
    '''Test start forms'''

    # render html
    return render(
        request,
        'vote/start.html',
        {'active_nav': 'start', },
    )