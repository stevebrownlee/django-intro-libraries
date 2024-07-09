from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the view function based on the request
        view_func = request.resolver_match.func

        # Check if the view allows unauthenticated access
        if getattr(view_func, 'nologin', False):
            return self.get_response(request)

        # Check if the user is authenticated
        if not request.user.is_authenticated and request.path != reverse('register'):
            return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)
