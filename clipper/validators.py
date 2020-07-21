from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

def validate_unique_username(username):
    try:
        u = User.objects.get(username=username)
        if u is not None:
            raise ValidationError(
                _('Username "%(username)s" already exists'),
                params={'username': username}
            )
    except User.DoesNotExist:
        pass