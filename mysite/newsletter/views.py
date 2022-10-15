from django.shortcuts import render


def news(request):
    return render(request, 'newsletter/news.html', context={
        'title': 'Новини'
    })
