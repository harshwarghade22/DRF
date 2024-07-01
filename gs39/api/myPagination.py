from rest_framework.pagination import LimitOffsetPagination

class CustomPagination(LimitOffsetPagination):
    default_limit=7
    limit_query_param='p'
    
