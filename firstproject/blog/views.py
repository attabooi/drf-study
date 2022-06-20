import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from blog.models import Article, Category
from user.models import User

from datetime import datetime, timedelta
from django.utils import timezone

from user.serializers import UserSerializer

from drf_project.permissions import RegistedMoreThanSevenDaysUser, IsAdminOrIsAuthenticatedPostOnly

class ArticleView(APIView): # CBV 방식
    # permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능
    permission_classes = [IsAdminOrIsAuthenticatedPostOnly]
    def get(self, request):
        permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 
        # user = request.user

        today = timezone.now()
        articles = Article.objects.filter(start_date__gte=(datetime.today() - timedelta(minutes=1))).order_by("start_date")
        # 작성된지 3일이 지나지 않은 게시물만 출력
        titles = [article.title for article in articles]

        # return Response(UserSerializer(all_users, many=True).data)
        return Response({"article_list": titles})
    
    def post(self, request):
        
        
        
        title = request.data.get('title','')
        categories = request.data.get('categories','')
        body = request.data.get('body','')
        start_date = request.data.get('start_date','')

        if len(title) <= 5:
            return Response({'error': 'title이 5글자 이하라면 글을 작성할 수 없습니다.'})

        if len(body) <= 20:
            return Response({'error': '글 길이가 20글자 이하라면 글을 작성할 수 없습니다.'})

        if categories is not None:
            create_article = Article.objects.create(
            author = request.user,
            title = title,
            body = body,
            start_date = start_date,
        )
            print(categories)
            categories = Category.objects.get(category=categories)


            
            create_article.save()

            return Response({'message': '글 작성 성공!'})
        else:
            return Response({'error': '카테고리를 지정해주세요.'})


    def put(self, request):
        return Response({'message': 'put method!!'})

    def delete(self, request):
        return Response({'message': 'delete method!!'})
