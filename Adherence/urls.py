from . import views
from django.urls import path


   

urlpatterns = [
    
     path('', views.index,name='index'),
     path('zpp/',views.apploadZpp,name='zpp'),
     path('material/',views.apploadmaterial,name='material'),

]
