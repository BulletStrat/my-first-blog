from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from blog.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'published_date',
        ]


class PostListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
    )
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'url',
            'author',
            'title',
            'published_date',
        ]
    def get_author(self,obj):
        return str(obj.author.username)

class PostDetailSerializer(ModelSerializer):
    author = SerializerMethodField()
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'text',
            'published_date',
        ]

    def get_author(self, obj):
        return str(obj.author.username)

