from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ArticleSerializer(serializers.ModelSerializer):
    """
    serializer.Serializer需要我们手动定义字段
    serializer.ModelSerializer会自动根据模型定义字段
    """
    # 当需要隐藏author时
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # author = UserSerializer(read_only=True)
    status = serializers.ReadOnlyField(source='get_status_display')
    cn_status = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'
        # 不希望用户自行修改，所以改成只读
        read_only_fields = ('id', 'create_date', 'author')
        depth = 1


    def get_cn_status(self, obj):
        if obj.status == 'p':
            return "已发表"
        elif obj.status == 'd':
            return "草稿"
        else:
            return ''
