from rest_framework import serializers
from main.models import *



# Serializers

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'course', 'title']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id', 
            'module', 
            'name', 
            'duration', 
            'video_link', 
            'homework_type', 
            'homework_content'
        ]



# Banner Serializer
class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'description', 'image', 'is_active', 'created_at', 'updated_at']

class LessonSerializer(serializers.ModelSerializer):
    homework = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'name', 'duration', 'video_link', 'homework']

    def get_homework(self, obj):
        return {
            "type": obj.homework_type,
            "content": eval(obj.homework_content)  # String bo'lsa, JSON formatga o'tkazish
        }


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'lessons']



# CourseType Serializer
class CourseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseType
        fields = ['id', 'name', 'description']


# Course Serializer
class CourseSerializer(serializers.ModelSerializer):
    course_type = CourseTypeSerializer()  # Nested serializer for course type

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'course_type', 'start_date', 'end_date', 'price']


# News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'created_at', 'image', 'link']


# Subject Serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name', 'description']


# Teacher Serializer
class TeacherSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()  # Nested serializer for subject

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'subject', 'bio', 'photo']


# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'message']


# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'message']


# News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'created_at', 'image', 'link']

# Subject Serializer



