from rest_framework import serializers
from .models import Comment, People


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'full_comment']


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ['full_name', 'phone_number', 'written_date']


