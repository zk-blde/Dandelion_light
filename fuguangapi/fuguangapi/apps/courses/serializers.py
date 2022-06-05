from rest_framework import serializers
from .models import CourseDiretion,CourseCategory,Course
class CourseDiretionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDiretion
        fields = ["id","name"]

class CourseCategoryModelSerliazer(serializers.ModelSerializer):
    """课程分类的序列化器"""
    class Meta:
        model = CourseCategory
        fields = ["id", "name"]


class CourseModelSerializer(serializers.ModelSerializer):
    """课程信息的序列化器"""
    class Meta:
        model = Course
        fields = ["id","name","course_cover","level","students","status","pub_lessons","price","discount"]