from rest_framework import serializers

from .models import TestingDataBase

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body')
        model = TestingDataBase