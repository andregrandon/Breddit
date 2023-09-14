from django.contrib.auth import get_user_model


User = get_user_model()


USER_1 = {
    'email': 'john@test.com',
    'password': 'testpassword'
}

USER_2 = {
    'email': 'emma@test.com',
    'password': 'testpassword'
}


def ensure_user(user_data, active=True):
    password = user_data.get('password', None)
    user = User.objects.create(**user_data)
    user.set_password(password)
    user.is_active = active
    user.save()
    return user
