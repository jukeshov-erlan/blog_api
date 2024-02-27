from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CommentView, RatingView

router = SimpleRouter()
router.register('comments', CommentView)
router.register('ratings', RatingView)

urlpatterns = [
    path('', include(router.urls))
]