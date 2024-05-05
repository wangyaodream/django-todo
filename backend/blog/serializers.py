from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model


User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    """
    serializer.Serializer
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=90)
    body = serializers.CharField(required=False, allow_blank=True)
    author = serializers.ReadOnlyField(source="author.id")
    status = serializers.ChoiceField(choices=Article.STATUS_CHOICES, default='p')
    create_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        """
        Create a article instance
        """
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Using validated_data to update a article instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

