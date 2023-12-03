from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerUser, name='register'),

    path('', views.home, name='home'),

    path('room/<pk>', views.room, name='room'),
    path('create-room', views.createRoom, name='create-room'),
    path('update-room/<pk>', views.updateRoom, name='update-room'),
    path('delete-room/<pk>', views.deleteRoom, name='delete-room'),
    path('delete-message/<pk>/', views.deleteMessage, name="delete-message"),
    path('update-user/', views.updateUser, name="update-user"),
    path('topics/', views.topicsPage, name="topics"),
    path('activity/', views.activityPage, name="activity"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile")
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
