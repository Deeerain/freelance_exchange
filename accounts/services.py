from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()


class UserAlreadyRegisteredError(Exception):
    pass


def get_user_by_pk(pk: int) -> USER_MODEL:
    return USER_MODEL.objects.get(pk=pk)


def user_register(username: str, email: str, password: str) -> USER_MODEL:
    try:
        user = USER_MODEL.objects.get(username=username, email=email)
        raise UserAlreadyRegisteredError

    except USER_MODEL.DoesNotExist:
        user = USER_MODEL(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
