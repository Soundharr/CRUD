from django.urls import path,include
from .views import *
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('view/<int:id>/',views.view,name='view'),
    path('update/image/<int:id>/',views.image,name='image'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('register',views.head,name='register'),
    path('login/',views.option,name='login'),

]
