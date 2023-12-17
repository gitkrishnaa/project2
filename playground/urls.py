from django.urls import path
from . import views   # it import view file


urlpatterns=[
    path('hello/',views.say_hello)
]
