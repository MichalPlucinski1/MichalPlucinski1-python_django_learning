from django.urls import path
from . import views

#URLConf
urlpatterns = {
    #path('playground/hello', views.say_hello) # inclusion by urls from main module
    path('hello/', views.say_hello)
}