from Articels_App.API.serializers import ArticleListSerializer,ArticleCreateSerializer , ArticleDetailSerializer , CommentDetail ,CommentList
from Articels_App.models import Article , Comment
from rest_framework.generics import ListAPIView, RetrieveAPIView ,CreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from Articels_App.API import paginations





class ArticleListViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer
    pagination_class =paginations.ArticlePageNumberPagination
    lookup_field = 'id'
    # @action(methods=['get'] , detail=True)
    # def tes(self , request ):
    #
    #     return Response("key")



class CommentListViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentDetail
    pagination_class =paginations.ArticlePageNumberPagination









class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    pagination_class =paginations.ArticlePageNumberPagination
class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

class ArticleCreateAPIView(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleCreateSerializer

class CommentListView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetail

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetail
