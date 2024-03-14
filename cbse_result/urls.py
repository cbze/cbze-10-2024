from core.views import *
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('result/<roll_no>/', result, name='result'),
]
