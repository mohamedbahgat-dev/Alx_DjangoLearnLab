from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

"Token.objects.create"
"get_user_model().objects.create_user"

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input': 'password'}, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email','password', 'password2', 'bio']
        extra_kwargs = {
            'password' : {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio = validated_data['bio']
        )     
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        username = data['username']
        password = data['password']
        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise serializers.ValidationError('Invalid username or password')
        data['user'] = user
        return data
            

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']
        read_only_fields = ['id', 'followers']