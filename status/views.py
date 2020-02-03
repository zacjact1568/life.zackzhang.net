from django.shortcuts import render


def permission_denied(request, exception):
    return render(request, 'status/403.html')


def page_not_found(request, exception):
    return render(request, 'status/404.html')


def server_error(request):
    return render(request, 'status/500.html')
