from rest_framework import serializers
from .models import CourseDiretion,CourseCategory
class CourseDiretionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDiretion
        fields = ["id","name"]

class CourseCategoryModelSerliazer(serializers.ModelSerializer):
    """课程分类的序列化器"""
    class Meta:
        model = CourseCategory
        fields = ["id", "name"]