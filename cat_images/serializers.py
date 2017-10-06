from rest_framework import serializers
from .models import CatImage


class ModelImageSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = CatImage
        fields = ('id', 'title', 'image_url', 'like_nums', 'created', 'width', 'height', 'image', 'uploader')


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=48)
    image_url = serializers.CharField(required=True, max_length=256)
    image = serializers.ImageField(required=False)
    like_nums = serializers.IntegerField(required=False)
    created = serializers.DateTimeField(required=False)
    author = serializers.IntegerField(required=False)
    describe = serializers.CharField(required=False, allow_blank=True, max_length=128, style={'base_template': 'textarea.html'})
    width = serializers.IntegerField(required=False)
    height = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return CatImage.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.image = validated_data.get('image', instance.image)
        instance.like_nums = validated_data.get('like_nums', instance.like_nums)
        instance.created = validated_data.get('created', instance.created)
        instance.author = validated_data.get('author', instance.author)
        instance.describe = validated_data.get('describe', instance.describe)
        instance.width = validated_data.get('width', instance.width)
        instance.height = validated_data.get('height', instance.height)
