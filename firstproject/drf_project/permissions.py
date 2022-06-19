from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta
from django.utils import timezone
# datetime field와 비교할때 (datetime)user.join_date > datetime.now **에러**
# datetime field와 비교할때 (datetime)user.join_date > timezone.now **에러**

class RegistedMoreThanThreeDaysUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        # date filed : 2020-10-2
        # datetime field : 2020-10-2 10:50:00

        print(f"user join date : {user.join_date}")
        print(f"now date : {datetime.now()}")
        print(f"three days ago date : {datetime.now() - timedelta(days=3)}")
        return bool(user.join_date < (timezone.now() - timedelta(minutes=3)))