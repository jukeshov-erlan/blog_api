'''
1. придумать архитектуру (отдельная логика для юзера, для постов, для комментариев, для лайков)
2. создаем новое приложение
3. в settings.py we have to registrate rest_framework and new app
4. create database
5. working with class in models.py
6. inside post app we have to create files serializers.py and urls.py
7. in models class we have to create new directory for images in main directory
8. 'from django.contrib.auth import get_user_model'     Return the User model that is active in this project.
9. create .env on main level and in settings.py import 'from decouple import config'
--. SECRET_KEY we have to move to .env.  in env. we have create variable and this variable we have to replace in settings.py (SECRET_KEY, NAME, USER, PASSWORD,)
11. then we have to go to views.py in our app and import 'from.models import *', 'from .serializers import *', 'from rest_framework.views import APIView
'
12.inside creating class and  write
class PostView(APIView):
    def get(self, request):
        queryset = Post.objects.all()

13. go to serializer and import 
from rest_framework.serializers import ModelSerializer

from .models import *

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

updating in views.py in class         
serializer = PostSerializer(queryset, many=True)
return Response(serializer, status=200)

14.  go to urls.py and 
'from django.urls import path
from .views import PostView

urlpatterns = [
    path('posts/', PostView.as_view())
    
]

14. then create superuser and make migrations and migrate 

15. then go to urls in main config and update 
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls'))
]

16. 
'''