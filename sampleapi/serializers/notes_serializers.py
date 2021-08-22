from rest_framework import serializers
from sampleapi.models.notes import Notes

class NotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notes
        fields = '__all__'