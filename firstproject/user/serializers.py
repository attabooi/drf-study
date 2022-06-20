from rest_framework import serializers

from user.models import User, UserProfile
from blog.models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    articles_user = serializers.SerializerMethodField()


    # category = serializer.SerializerMethodField()
    # def get_category(self, obj):
    #     return [category.name for category in obj.category.all()]
    
    def get_articles_user(self,obj):
        return obj.author.username

    class Meta:
        model = Article
        fields = ["title", "body", "articles_user"]

class CommentSerializer(serializers.ModelSerializer):
    comments_user = serializers.SerializerMethodField()

    def get_comments_user(self,obj):
        return obj.author.username
    class Meta:
        model = Comment
        fields = ["comment", "comments_user"]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user"]

class UserSerializer(serializers.ModelSerializer):
    article_set = ArticleSerializer(many=True)
    #articles = ArticleSerializer(many=True, source="article_set")
    comment_set = CommentSerializer(many=True)
    userprofile = UserProfileSerializer()
    print(comment_set)
    class Meta:
        model = User
        fields = ["username","userprofile","article_set","comment_set"]


