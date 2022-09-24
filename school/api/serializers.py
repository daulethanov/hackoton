from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'last_name', 'password', 'patronymic', 'iin', 'nubmer']


class CustomRegisterSerializer(RegisterSerializer):

    class Meta:
        model = User
        fields = ['email', 'username','last_name',  'password', 'patronymic','iin', 'nubmer', ]

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'patronymic': self.validated_data('patronymic', ''),
            'iin': self.validated_data('iin', ''),
            'numer': self.validated_data('number', '')
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        user.save()
        self.custom_signup(request, user)
        return user
