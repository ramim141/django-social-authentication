from django.contrib.auth import get_user_model

User = get_user_model()

def google_verified_user(backend, user, response, *args, **kwargs):
    """
    Marks a user as verified if their email is verified by Google.
    """
    if backend.name == 'google-oauth2':
        # The `email_verified` field is a boolean provided by Google.
        if response.get('email_verified', False):
            user.is_verified = True
            user.save()

def check_email_exists(backend, details, *args, **kwargs):
    """
    Checks if a user with the given email already exists.
    If so, returns the user to prevent creating a duplicate.
    """
    email = details.get('email')
    if email:
        try:
            user = User.objects.get(email=email)
            return {'user': user}
        except User.DoesNotExist:
            pass
    return None