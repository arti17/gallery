from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from webapp.models import Comment
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
