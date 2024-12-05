# urls.py
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import  *

# Swagger Schema View
schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@myapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

urlpatterns = [
    # Banner URLs
    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerRetrieveUpdateDestroyView.as_view(), name='banner-detail'),

    # CourseType URLs
    path('course-types/', CourseTypeListCreateView.as_view(), name='course-type-list-create'),
    path('course-types/<int:pk>/', CourseTypeRetrieveUpdateDestroyView.as_view(), name='course-type-detail'),

    # Course URLs
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),

    # News URLs
    path('news/', NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:pk>/', NewsRetrieveUpdateDestroyView.as_view(), name='news-detail'),

    # Subject URLs
    path('subjects/', SubjectListCreateView.as_view(), name='subject-list-create'),
    path('subjects/<int:pk>/', SubjectRetrieveUpdateDestroyView.as_view(), name='subject-detail'),

    # Teacher URLs
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherRetrieveUpdateDestroyView.as_view(), name='teacher-detail'),

    # Message URLs
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-detail'),

    # Contact URLs
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('modules/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDeleteView.as_view(), name='module-detail'),

    # Lesson endpoints
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDeleteView.as_view(), name='lesson-detail'),

    # Authentication URLs
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    
    # Swagger URLs
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
