from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone
from rest_framework.exceptions import APIException
from rest_framework import status

from argon2 import PasswordHasher


# datetime field와 비교할때 (datetime)user.join_date > datetime.now **에러**
# datetime field와 비교할때 (datetime)user.join_date > timezone.now **정상**

class RegistedMoreThanSevenDaysUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # date filed : 2020-10-2
        # datetime field : 2020-10-2 10:50:00

        # print(f"user join date : {user.join_date}")
        # print(f"now date : {datetime.now()}")
        # print(f"three days ago date : {datetime.now() - timedelta(days=7)}")
        return bool(user.is_authenticated and 
        request.user.join_date < (timezone.now() - timedelta(days=7)))

class GenericAPIException(APIException):
    def __init__(self, status_code, detail=None, code=None):
        self.status_code=status_code
        super().__init__(detail=detail, code=code)

class IsAdminOrIsAuthenticatedPostOnly(BasePermission):
    # admin 사용자는 모두 가능, 로그인 사용자는 조회만 가능
    SAFE_METHODS = ('POST', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if not user.is_authenticated:
            response = {
                "detail": "서비스를 이용하기 위해 로그인 해주세요."
            }
            raise GenericAPIException(status_code=status.HTTP_401_UNAUTHORIZED, detail=response)

        if user.is_authenticated and user.is_admin:
            return True
        
        elif not user or not user.is_authenticated:
            return False

        # date filed : 2020-10-2
        # datetime field : 2020-10-2 10:50:00

        # print(f"user join date : {user.join_date}")
        # print(f"now date : {datetime.now()}")
        # print(f"three days ago date : {datetime.now() - timedelta(days=7)}")
        return bool(user.is_authenticated and 
        request.user.join_date < (timezone.now() - timedelta(minutes=1)))