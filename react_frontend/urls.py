from django.urls import path
from .views import index

urlpatterns = [
    path('myindex/', index,name='myindex'),
  
]