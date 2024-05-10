from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model


User = get_user_model()


class ArticleSerializer(serializers.ModelSerializer):
    """
    serializer.Serializer需要我们手动定义字段
    serializer.ModelSerializer会自动根据模型定义字段
    """
    # 当需要隐藏author时
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('id', 'create_date', 'author')


