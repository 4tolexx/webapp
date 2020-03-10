from allauth.account import urls
from.import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static





app_name = 'tee'



urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('career/', views.career, name = 'career'),
    path('login/', views.login.as_view(), name = 'login'),
    path('signup/', views.signup.as_view(), name = 'signup'),
    path('logout/', views.logout.as_view(), name = 'logout'),
    path('job/', views.JobCreate.as_view(), name='job'),
    path('detail/<int:pk>/', views.JobDetail.as_view(), name = 'job-detail'),
    path('update/<int:pk>/', views.JobUpdate.as_view(), name = 'job-update'),
   
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
