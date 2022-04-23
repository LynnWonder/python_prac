from rest_framework import status
from rest_framework.exceptions import APIException


class SnippetNotExistException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '不存在的代码段 id'
    default_code = 'snippet_not_exist_exception'
