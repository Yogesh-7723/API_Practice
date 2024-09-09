from rest_framework.pagination import LimitOffsetPagination,CursorPagination

# class MyLimitPagination(LimitOffsetPagination):
#     default_limit = 3
#     max_limit = 6
#     limit_query_param = 'mylimit'
#     offset_query_param = 'myoffset'

class MyCursorPagination(CursorPagination):
    page_size = 3
    ordering = 'name'