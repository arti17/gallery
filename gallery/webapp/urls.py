from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('', views.PhotosView.as_view(), name='index'),
    path('photo/<int:pk>/', views.PhotoDetail.as_view(), name='photo_detail'),
    path('photo/add/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/edit/<int:pk>', views.PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/delete/<int:pk>', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
