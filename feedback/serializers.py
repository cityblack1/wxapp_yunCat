from rest_framework import serializers

from .models import FeedBack, Contact


class FeedBackSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = FeedBack
        fields = ('created', 'title', 'content_type', 'object_id', 'content',
                  'uploader', 'id', 'has_processed')


class ContactSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='uploader.username')

    class Meta:
        model = Contact
        fields = ('created', 'title', 'content', 'uploader', 'id', 'has_processed')