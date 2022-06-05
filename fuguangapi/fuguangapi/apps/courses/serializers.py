from rest_framework import serializers
from .models import CourseDiretion
class CourseDiretionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDiretion
        fields = ["id","name"]