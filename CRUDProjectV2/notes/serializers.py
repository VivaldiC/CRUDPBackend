from rest_framework import serializers
from .models import Notes

class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('id','task_title', 'description')