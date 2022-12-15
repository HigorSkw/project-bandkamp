from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= [
            'id', 'username', 'email', 'first_name','last_name', 'password', 'is_superuser'
            ]
        
        extra_kwargs = {"password": {"write_only": True}}

    def email_already_exists(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This field must be unique")
        
        return value


    def create(self, validated_data: dict) -> User:
        
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()

        return instance