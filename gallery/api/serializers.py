from rest_framework import serializers
from webapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    author = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'photo', 'author', 'create_at')

    def create(self, request):
        photo = request['photo']
        author = self.context['request'].user
        text = request['text']
        comment = Comment.objects.create(author=author, photo=photo, text=text)
        return comment
