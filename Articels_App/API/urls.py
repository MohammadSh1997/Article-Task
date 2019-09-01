from Articels_App.API import views
from django.urls import path , include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article' , views.ArticleListViewSet , base_name = 'ARTICLE')
router.register('comment' , views.CommentListViewSet , base_name = 'COMMENT')

app_name='Art'
urlpatterns = [
path('root/' , include(router.urls)),




path('' , views.ArticleListAPIView.as_view() , name='ArticleListApi'),
path('<int:pk>' , views.ArticleDetailAPIView.as_view() , name='ArticleDetailApi'),
path('create/' , views.ArticleCreateAPIView.as_view() , name='ArticleCreateApi'),
path('comment/' , views.CommentListView.as_view() , name='CommentList'),
path('comment/create' , views.CommentCreateAPIView.as_view() , name='CreateComment'),
]
