from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Comment, Photo, Like
from api.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        photo_pk = kwargs.get('pk')
        try:
            like = Like()
            like.author_id = self.request.user.pk
            like.photo_id = photo_pk
            like.save()
        except:
            return Response({'status': 'Лайк уже есть.'})

        photo = Photo.objects.get(pk=photo_pk)
        photo.likes += 1
        photo.save()
        return Response({'id': photo.pk, 'rating': photo.likes, 'status': 'ok'})


class DizlikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        photo_pk = kwargs.get('pk')

        like = Like.objects.filter(author=request.user.pk)
        if like:
            like.delete()
            photo = Photo.objects.get(pk=photo_pk)
            photo.likes -= 1
            photo.save()
            return Response({'id': photo.pk, 'rating': photo.likes, 'status': 'ok'})
        return Response({'status': 'error'})
