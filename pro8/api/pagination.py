from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'position'
    page_size_query_param = 'record'
    max_page_size = 5
    last_page_strings = 'end_page'