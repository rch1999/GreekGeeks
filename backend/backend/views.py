from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
import requests


@require_http_methods(["GET"])
def activate(request):
    """Placeholder for email verification."""
    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')

    url = f'{request.scheme}://{request.get_host()}/api/users/email/'
    body = {
        'uidb64': uidb64,
        'token': token
    }
    response = requests.post(url, json=body)

    return redirect('/')
