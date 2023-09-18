
from rest_framework.pagination import PageNumberPagination,CursorPagination


class GenrePaginator(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 3
    

class GenreCursorPaginator(CursorPagination):
    page_size = 4