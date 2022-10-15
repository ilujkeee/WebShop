from django.shortcuts import render


def sign_in(request):
    return render(request, 'accounts/sign_in.html', context={
        'title': 'Вхід'
    })


def sign_up(request):
    return render(request, 'accounts/sign_up.html', context={
        'title': 'Реєстрація'
    })


def sign_out(request):
    return render(request, 'accounts/sign_out.html', context={
        'title': 'Вихід'
    })


def profile(request):
    return render(request, 'accounts/profile.html', context={
        'title': 'Профіль'
    })
