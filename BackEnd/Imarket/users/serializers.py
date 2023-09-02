from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'user_type', 'phone_number', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # for hiding password
        }

    def create(self, validated_data):  # кэширование
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super().get_token(user)
        token['user_type'] = user.user_type

        return token

    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     refresh = self.get_token(self.user)
    #     data['access'] = str(refresh.access_token)
    #     data['user_type'] = self.user.user_type  # Add user_type to payload data
    #     return data
