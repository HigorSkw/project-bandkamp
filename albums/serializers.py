from rest_framework import serializers

from .models import Album
from users.serializers import UserSerializer

class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = ['id', 'name', 'year', 'user_id']
        depth = 1


