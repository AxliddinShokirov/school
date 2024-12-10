# urls.py
from django.urls import path, include
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import  *

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",  # API nomi
        default_version='v1',   # API versiyasi
        description="API for managing teachers, courses, news, and feedback. Provides authentication (login/register) functionalities.",  # API tavsifi
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),  # Kontakt ma'lumotlari
        license=openapi.License(name="BSD License"),  # Litsenziya
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # API uchun umumiy ruxsat
)

urlpatterns = [
    # Banner URLs
    path('banners/', BannerListCreateView.as_view(), name='banner-list-create'),
    path('banners/<int:pk>/', BannerRetrieveUpdateDestroyView.as_view(), name='banner-detail'),

    # CourseType URLs
    path('course-types/', CourseTypeListCreateView.as_view(), name='course-type-list-create'),
    path('course-types/<int:pk>/', CourseTypeRetrieveUpdateDestroyView.as_view(), name='course-type-detail'),

    path('course-details/',CourseDetailListCreateView.as_view(), name='course-detail-list-create'),
    path('course-details/<int:pk>/', CourseDetailRetrieveUpdateDestroyView.as_view(), name='course-detail-retrieve-update-destroy'),


    # Course URLs
    path('curescreat/',  CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),
    path('course-type/<int:course_type_id>/courses/', CourseTypeWithCoursesView.as_view(), name='course-type-with-courses'),


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
    path('thoughts/', MessageListCreateView.as_view(), name='message-list-create'),
    path('thoughts/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-detail'),

    # Contact URLs
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactRetrieveUpdateDestroyView.as_view(), name='contact-detail'),

    path('modules/', ModuleListCreateView.as_view(), name='module-list-create'),
    path('modules/<int:pk>/', ModuleRetrieveUpdateDeleteView.as_view(), name='module-detail'),

    # Lesson endpoints
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDeleteView.as_view(), name='lesson-detail'),
    path('education-statistics/', EducationStatisticsRetrieveUpdateDestroyView.as_view(), name='education-statistics-list'),
   
    path('education-statistics/<int:pk>/', EducationStatisticsRetrieveUpdateDestroyView.as_view(), name='education-statistics-detail'),

    path('EmailSubscription/', EmailSubscriptionListview.as_view(), name='email-list'),
    path('emailSubscription/<int:pk>/', EmailSubscriptionRetrieveUpdateDestroyView.as_view(), name='email-detail'),


    # Authentication URLs
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
