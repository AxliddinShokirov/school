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




# Contact CRUD API
class ContactListCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve a list of contacts or create a new contact.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new contact.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    

class CourseDetailView(RetrieveAPIView):
    queryset = Course.objects.prefetch_related('modules__lessons')
    serializer_class = CourseSerializer

class ContactRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a contact.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a contact.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a contact.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    




# News CRUD API
class NewsListCreateView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    @swagger_auto_schema(operation_description="Retrieve a list of news or create a new one.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new news item.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a news item.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a news item.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a news item.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Subject CRUD API
class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve a list of subjects or create a new one.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new subject.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class SubjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a subject.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a subject.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a subject.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Teacher CRUD API
class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve a list of teachers or create a new one.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new teacher.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a teacher.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a teacher.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a teacher.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




# Message CRUD API
class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve a list of messages or create a new one.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new message.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)





class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Retrieve, update, or delete a message.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a message.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a message.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




# Banner CRUD API
class BannerListCreateView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of banners or create a new one.",
        responses={200: BannerSerializer, 400: 'Bad request'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new banner.",
        request_body=BannerSerializer,
        responses={201: BannerSerializer, 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




class BannerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve, update, or delete a banner.",
        responses={200: BannerSerializer, 400: 'Bad request', 404: 'Not found'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a banner.",
        request_body=BannerSerializer,
        responses={200: BannerSerializer, 400: 'Bad request'}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a banner.",
        responses={204: 'No content', 404: 'Not found'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




# CourseType CRUD API
class CourseTypeListCreateView(generics.ListCreateAPIView):
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer
    permission_classes = [IsAuthenticated]
    
    filter_backends = [SearchFilter]
    search_fields = ['name']  # Bu yordamida kurs turlari nomi bo'yicha qidirish mumkin

    @swagger_auto_schema(
        operation_description="Retrieve a list of course types.",
        responses={200: CourseTypeSerializer(many=True), 400: 'Bad request'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new course type.",
        request_body=CourseTypeSerializer,
        responses={201: CourseTypeSerializer, 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class CourseTypeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CourseType.objects.all()
    serializer_class = CourseTypeSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve, update, or delete a course type.",
        responses={200: CourseTypeSerializer, 400: 'Bad request', 404: 'Not found'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a course type.",
        request_body=CourseTypeSerializer,
        responses={200: CourseTypeSerializer, 400: 'Bad request'}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a course type.",
        responses={204: 'No content', 404: 'Not found'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




# Course CRUD API
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of courses or create a new one.",
        responses={200: CourseSerializer, 400: 'Bad request'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new course.",
        request_body=CourseSerializer,
        responses={201: CourseSerializer, 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve, update, or delete a course.",
        responses={200: CourseSerializer, 400: 'Bad request', 404: 'Not found'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a course.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer, 400: 'Bad request'}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a course.",
        responses={204: 'No content', 404: 'Not found'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)





# Module List/Create API
class ModuleListCreateView(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of modules or create a new module.",
        responses={200: ModuleSerializer(many=True), 400: 'Bad request'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new module.",
        request_body=ModuleSerializer,
        responses={201: ModuleSerializer, 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




# Lesson List/Create API
class LessonListCreateView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a list of lessons or create a new lesson.",
        responses={200: LessonSerializer(many=True), 400: 'Bad request'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new lesson.",
        request_body=LessonSerializer,
        responses={201: LessonSerializer, 400: 'Bad request'}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)




# Module Retrieve/Update/Delete API
class ModuleRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific module.",
        responses={200: ModuleSerializer, 404: 'Not found'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update details of a specific module.",
        request_body=ModuleSerializer,
        responses={200: ModuleSerializer, 400: 'Bad request'}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a specific module.",
        responses={204: 'No content', 404: 'Not found'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)




# Lesson Retrieve/Update/Delete API
class LessonRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve details of a specific lesson.",
        responses={200: LessonSerializer, 404: 'Not found'}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update details of a specific lesson.",
        request_body=LessonSerializer,
        responses={200: LessonSerializer, 400: 'Bad request'}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a specific lesson.",
        responses={204: 'No content', 404: 'Not found'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    


# "log_in"
@api_view(['POST'])
def log_in(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({
                'success': False,
                'error': 'Username and password are required.'
            }, status=400)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({
                'success': False,
                'error': 'User does not exist. Please check your username.'
            }, status=404)

        user = authenticate(username=username, password=password)
        if user is not None:
            token_key, _ = Token.objects.get_or_create(user=user)
            context = {
                'success': True,
                'username': user.username,
                'key': token_key.key
            }
        else:
            context = {
                'success': False,
                'error': 'Invalid password. Please check your password.'
            }
    except Exception as e:
        return Response({
            'success': False,
            'error': f"An unexpected error occurred: {str(e)}"
        }, status=500)

    return Response(context)


@swagger_auto_schema(
    operation_description="Log out a user by deleting the token.",
    responses={200: 'Success'},
    method='GET'
)

# 'log_out'
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def log_out(request):
    Token.objects.get(user=request.user).delete()
    return Response({'success': True})

# register
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



