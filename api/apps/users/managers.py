from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create(self, username, telegram_id, password=None, **extra_fields):
        if not username:
            raise ValueError(_('The username must be set'))
        return self.create_user(username, telegram_id, password, **extra_fields)

    def create_user(self, username, telegram_id, password, **extra_fields):
        user = self.model(username=username, telegram_id=telegram_id, **extra_fields)
        if password:
            user.set_password(password)
        else:
            user.set_password(username)
        user.save()
        return user
