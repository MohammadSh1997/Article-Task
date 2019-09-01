from rest_framework.pagination import PageNumberPagination , LimitOffsetPagination


class ArticlePagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
class ArticlePageNumberPagination(PageNumberPagination):
    page_size = 2
