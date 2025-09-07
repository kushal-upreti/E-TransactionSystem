# accounts/serializers.py
from dj_rest_auth.serializers import PasswordResetSerializer 
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.core.mail import send_mail
from rest_framework import serializers
from .models import UserProfile
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.conf import settings



class UserProfileSerializer(serializers.ModelSerializer):
    avatar=serializers.ImageField(required=False)
    class Meta:
        model=UserProfile
        fields=[
            'id', 'name', 'username', 'email', 'phone_no', 
            'avatar', 'created_at'
        ]
    
class CustomUserRegistrationSerializer(RegisterSerializer):
    name=serializers.CharField(max_length=200, required=True)
    phone_no=serializers.CharField(max_length=20, required=True)
    avatar=serializers.ImageField(required=False)
    address=serializers.CharField(max_length=200, allow_blank=True)
    
    def validate_phone_no(self, value):
        if UserProfile.objects.filter(phone_no=value).exists():
            raise serializers.ValidationError('Already created with this id')
        
        return value

    def save(self, request):
        user= super().save(request)
        user.name=self.validated_data.get('name')
        user.phone_no=self.validated_data.get('phone_no')
        user.avatar=self.validated_data.get('avatar', 'avatar.svg')
        user.address=self.validated_data.get('address')
        user.save()
        return user


# serializers.py
# from dj_rest_auth.serializers import PasswordResetSerializer

# class CustomPasswordResetSerializer(PasswordResetSerializer):
#     def get_email_options(self):
#         return {
#             'email_template_name': 'registration/password_reset_email.html',
#         }

#     def save(self, **kwargs):
#         frontend_url = 'http://localhost:3000/reset-password/{uid}/{token}/'
#         kwargs['use_https'] = True
#         kwargs['from_email'] = None
#         kwargs['request'] = self.context.get('request')
#         kwargs['html_email_template_name'] = None
#         kwargs['extra_email_context'] = {'frontend_url': frontend_url}
#         super().save(**kwargs)



class CustomPasswordResetSerializer(PasswordResetSerializer):

    def save(self, **kwargs):
        request = self.context.get('request')
        email = self.validated_data['email']

        # Use PasswordResetForm to get the users
        form = PasswordResetForm(data={'email': email})
        if form.is_valid():
            for user in form.get_users(email):
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))

                frontend_url = f"http://localhost:3000/password-reset-confirm/{uid}/{token}/"

                context = {
                    'frontend_reset_url': frontend_url,
                    'user': user,
                }

                subject = render_to_string('accounts/password_reset_subject.txt', context)
                subject = ''.join(subject.splitlines())
                message = render_to_string('accounts/password_reset_email.html', context)

                send_mail(subject, message, None, [user.email])