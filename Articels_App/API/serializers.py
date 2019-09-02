from rest_framework.serializers import ModelSerializer , HyperlinkedIdentityField , SerializerMethodField , HyperlinkedModelSerializer
from Articels_App.models import Article , Comment

class ArticleListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
    view_name = 'API:ArticleDetailApi',
    lookup_field = 'pk'
    )
    publisher = SerializerMethodField()
    class Meta():
        model = Article
        fields = [
        'url',
        'publisher',
        'title',
        ]
    def get_publisher(self , obj):
        return str(obj.publisher.user)

class CommentList(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
        'art',
        'comment',
        ]

class CommentDetail(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
        'art',
        'comment',
        ]
        depth=1


class ArticleDetailSerializer(ModelSerializer):
    com = CommentList(many=True , read_only=True)
    publisher = SerializerMethodField()
    class Meta:
        model = Article
        fields = [
        'publisher',
        'title',
        'article',
        'com'
        ]

    def get_publisher(self , obj):
        return str(obj.publisher.user)

class ArticleCreateSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields='__all__'
