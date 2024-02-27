from rest_framework.serializers import ModelSerializer, ValidationError, ReadOnlyField
from review.serializers import CommentSerializer
from review.models import Comment
from django.db.models import Avg
from .models import *

class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = ('title',)

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('title',)




class PostSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.name')
    class Meta:
        model = Post
        fields = '__all__'
    
    def validate_title(self, title):
        if self.Meta.model.objects.filter(title=title).exists():
            raise ValidationError(
                'Такой заголовок уже существует'
            )
        return title
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['test'] = 'test'
    #     representation['tags'] = instance.tags.all()
    #     return representation

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # representation['comments']=CommentSerializer(instance.comments.all(), many=True).data
        representation['comments'] = CommentSerializer(
            Comment.objects.filter(post=instance.pk), many=True
        ).data
        representation['rating'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['likes'] = instance.likes.count()
        return representation
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return super().create(validated_data)
        # post = Post.objects.create(author=user, **validated_data)
        # post.tags.add(*tags)
        # return post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']

