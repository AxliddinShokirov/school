
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import *
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.generics import RetrieveAPIView

from main.models import *
from .serializers import *

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import  *
from main.models import *
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter


class EmailSubscriptionListview(generics.ListCreateAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

class EmailSubscriptionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer
    
 
    

class BannerListCreateView( generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class CourseTypeListCreateView(generics.ListCreateAPIView):
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer

class CourseTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class CourseDetailListCreateView(generics.ListCreateAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer

class CourseDetailRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseDetail.objects.all()
    serializer_class = CourseDetailSerializer




class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']


class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter]

    search_fields = ['title', 'content']

class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']


class  SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class SubjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'designation']

class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'designation']


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Thoughts.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thoughts.objects.all()
    serializer_class = MessageSerializer

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_number']

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name', 'email', 'phone_number']

class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class  ModuleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [SearchFilter]

    search_fields = ['title', 'description']


class EducationStatisticsRetrieveUpdateDestroyView(generics.ListCreateAPIView ,generics.RetrieveUpdateDestroyAPIView):
    queryset = EducationStatistics.objects.all()
    serializer_class = EducationStatisticsSerializer


class CourseTypeWithCoursesView(APIView):
    def get(self, request, course_type_id):
        try:
            course_type = CourseType.objects.get(id=course_type_id)
            courses = Course.objects.filter(course_type_id=course_type_id)
            course_type_data = CourseTypeSerializer(course_type).data
            courses_data = CourseSerializer(courses, many=True).data

            # Frontend uchun qulay formatda ma'lumotlarni birlashtiramiz
            response_data = {
                "course_type": course_type_data,
                "courses": courses_data
            }
            return Response(response_data, status=status.HTTP_200_OK)
        except CourseType.DoesNotExist:
            return Response({"error": "CourseType not found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def log_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        # user bilan token olish
        token_key, _ = Token.objects.get_or_create(user=user)
        context = {
            'success': True,
            'username': user.username,
            'key': token_key.key
        }
    else:
        context = {
            'success': False,
            'error': 'Invalid credentials.'
        }
    return Response(context)

@api_view(['POST'])
def log_out(request):
    token = request.data.get('token')
    if token is not None:
        try:
            token_key = Token.objects.get(key=token)
            token_key.delete()
            context = {
                'success' : True,
                'message' : 'Token deleted successfully.'
            }
        except:
            context = {
                'success' : False,
                'error' : 'Invalid token.'
            }
    else:
        context = {
            'success' : False,
            'error' : 'No token provided.'
        }
    return Response(context)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def say_hello(request):
    return Response('Hello, World!')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def log_out(request):
    Token.objects.get(user=request.user).delete()
    return Response({'success':True})


@api_view(['POST'])
def register(request):
    try:

        username = request.data.get('username')
        password = request.data.get('password')


        user = User.objects.create(username=username,
                                    password=password)
        token = Token.objects.create(user=user)

        context = {
            'success': True,
            'username': user.username,
            'password': password,
            'id': user.id,
            'token' : token.key
        }
    except Exception as e:

        context = {
            'success': False,
            'error': str(e),
        }

    return Response(context)

