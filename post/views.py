# from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import CursorPagination
from rest_framework.decorators import action
from review.models import Likes
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .permissions import IsAuthorPermission


class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    permission_classes = [IsAdminUser]

class CustomCursorPagination(CursorPagination):
    page_size = 2
    ordering = '-created_at'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title', 'body', ]
    # ordering_fields = ['title']
    pagination_class = CustomCursorPagination

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = [AllowAny]
        elif self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorPermission]
        return [permission() for permission in permissions]

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class

    @action(methods=['POST'], detail=True, permission_classes=[IsAuthenticated])
    def like(self,request, pk=None):
        post = self.get_object()
        user = request.user
        try:
            like = Likes.objects.get(post=post, author=user)
            like.delete()
            message = 'dislike'
        except Likes.DoesNotExist:
            like = Likes.objects.create(post=post, author=user)
            message = 'liked'
        return Response(message, status=200)
    

        

# class PostView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category', 'tags']
    # search_fields = ['title', 'body', ]
    # ordering_fields = ['title']
#     # serializer_class = PostSerializer

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return PostListSerializer
#         return PostSerializer
        
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# Create your views here.
# class PostView(APIView):
#     def get(self, request):
#         queryset = Post.objects.all()
#         serializer = PostSerializer(queryset, many=True)
#         return Response(serializer, status=200)
    
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
    
#     def put(self, request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=400)
    
#     def patch(self,request, pk):
#         post = Post.objects.get(pk=pk)
#         serializer = PostSerializer(post, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=200)
#         return Response(status=400)
        
#     def delete(self,request, pk):
#         post = Post.objects.get(pk=pk)
#         post.delete()
#         return Response(status=204)


