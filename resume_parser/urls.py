from django.urls import path
from . import views   # it import view file


urlpatterns=[
    path('parse/',views.say_hello),
    path('upload/',views.upload_file),
]
