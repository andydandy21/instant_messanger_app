from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from dj_rest_auth.forms import AllAuthPasswordResetForm

if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account import app_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.forms import default_token_generator
    from allauth.account.utils import (user_pk_to_url_str, user_username)


class CustomPasswordResetForm(AllAuthPasswordResetForm):

    def save(self, request, **kwargs):
        current_site = get_current_site(request)
        email = self.cleaned_data['email']
        token_generator = kwargs.get('token_generator', default_token_generator)

        for user in self.users:

            temp_key = token_generator.make_token(user)

            # save it to the password reset model
            # password_reset = PasswordReset(user=user, temp_key=temp_key)
            # password_reset.save()

            # send the password reset email

            # previous url creator
            # path = reverse(
            #    'password_reset_confirm',
            #    args=[user_pk_to_url_str(user), temp_key],
            # )
            # url = build_absolute_uri(request, path)
            
            # #additional code added by yours truly
            default_url = 'password/reset/confirm/'
            custom_frontend_url = f'{settings.FRONTEND_URL}{default_url}{user_pk_to_url_str(user)}/{temp_key}/'

            context = {
                'current_site': current_site,
                'user': user,
                'password_reset_url': custom_frontend_url,
                'request': request,
            }
            if app_settings.AUTHENTICATION_METHOD != app_settings.AuthenticationMethod.EMAIL:
                context['username'] = user_username(user)
            get_adapter(request).send_mail(
                'account/email/password_reset_key', email, context
            )
        return self.cleaned_data['email']