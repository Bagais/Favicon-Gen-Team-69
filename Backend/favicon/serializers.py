from rest_framework import serializers

from favicon.models import Favicon, Icon
from user_control.serializers import UserSerializer

class  IconSerializer(serializers.ModelSerializer):
    class Meta:
        model = Icon
        fields = ("icon", "favicon")
        extra_kwargs = {'favicon': {'write_only': True}}


class FaviconSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)

    author = UserSerializer(read_only=True)

    icons = IconSerializer(many=True, read_only=True)

    class Meta:
        model = Favicon
        fields ='__all__'

class TextPreviewSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=50)
    font_size = serializers.IntegerField()
    text_color = serializers.ListField()
    background_color = serializers.ListField()
    url = serializers.URLField()

class EmojiPreviewSerializer(serializers.Serializer):
    emoji = serializers.CharField()   
    text_color = serializers.ListField()
    background_color = serializers.ListField()
    url = serializers.URLField()
 

 

        
        