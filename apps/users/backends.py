from django.contrib.auth.backends import ModelBackend

from .models import User


class DommarBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        password = kwargs.get('password', None)
        try:
            user = User.objects.get(username=username)
            if password and user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            pass
