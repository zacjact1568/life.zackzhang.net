from django.shortcuts import render


def forbidden(request):
    return render(request, 'status/403.html')


def page_not_found(request):
    return render(request, 'status/404.html')


def internal_server_error(request):
    return render(request, 'status/500.html')
