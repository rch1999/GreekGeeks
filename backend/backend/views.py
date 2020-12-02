from django.views.decorators.http import require_http_methods
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from api.tokens import email_verification_token_generator
from django.shortcuts import redirect

User = get_user_model()


@require_http_methods(["GET"])
def activate(request):
    uidb64 = request.GET.get('uidb64')
    token = request.GET.get('token')
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None

    if user is not None and \
       email_verification_token_generator.check_token(user, token):
        user.email_verified = True
        user.save()

    return redirect('/')
