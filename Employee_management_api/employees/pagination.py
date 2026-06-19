from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10                  # Serve 10 records at a time
    page_size_query_param = 'size'  # User can request more: ?size=50
    max_page_size = 100             # Cap it at 100 for performance safety
