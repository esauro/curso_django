from django.contrib.auth import get_user_model

__author__ = 'esauro'


class HardcodedBackend(object):

    def authenticate(self, username=None, password=None):
        user_cls = get_user_model()

        if username == "esauro" and password:
            return user_cls.objects.get(username="admin")
        return None

    def get_user(self, user_id):
        user_cls = get_user_model()
        try:
            return user_cls.objects.get(pk=user_id)
        except user_cls.DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        if user_obj.username == "esauro":
            return True
        return False