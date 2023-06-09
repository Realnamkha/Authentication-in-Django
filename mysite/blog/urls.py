from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.home,name='home'),
    path('about/', views.about,name='about'),
    path('register/', views.registerUser,name='register'),
    path('login/', views.loginUser,name='login'),
    path('logout/', views.logoutUser,name='logout'),
    path('profile/<str:pk>/', views.profile,name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)