from django.contrib import admin
from django.urls import path

from generator_qr import views
name_app = 'qrcode'
urlpatterns = [
    path('qrcode/<str:data>/', views.generate_qrcode, name='generate_qrcode'),

]

