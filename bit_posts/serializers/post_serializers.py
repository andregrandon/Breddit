from rest_framework import serializers
from bit_posts.models import Post
from bit_users.serializers import user_serializers


class PostSerializer(serializers.ModelSerializer):
    user = user_serializers.UserSerializer(read_only=True)

    class Meta:
      model = Post
      fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(PostSerializer, self).create(validated_data)
    
      
class FindByIDSerializer(serializers.Serializer):
    pk = serializers.IntegerField()  

class UpvoteResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    liked = serializers.BooleanField()
    new_like_count = serializers.IntegerField()
