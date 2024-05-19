from djamgo.urls import path 
from . import views 

#URLConf
ulrpatterns = [
    path('playground/hello', views.say_hello) 
]