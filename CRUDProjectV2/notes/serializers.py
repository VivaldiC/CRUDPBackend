from rest_framework import serializers
from .models import Notes

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = ('pk','task_title', 'description')