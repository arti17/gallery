from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]
