from django.urls import path
from . import views

urlpatterns = [
    path('send-email/', views.send_email_ajax, name='send_email_ajax'),
    path('upload-files/', views.upload_files_home, name='upload_files_home'),
    path('upload-credentials/', views.upload_credentials, name='upload_credentials'),
    path('dataview/', views.dataview, name='dataview'),
    path('', views.home, name='home'), 
]
