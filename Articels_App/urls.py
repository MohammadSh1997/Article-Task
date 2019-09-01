from Articels_App import views
from django.urls import path

app_name='Art'
urlpatterns = [
path('' , views.ArticleListView.as_view() , name='ArticleList'),
path('<int:pk>' , views.ArticleDetailView.as_view() , name='ArticleDetail'),
path('CreateArticle/', views.ArticleCreateView.as_view() , name = 'CreateArticle'),
path('comment/<int:pk>/' , views.comment_to_article , name='comment'),


]
