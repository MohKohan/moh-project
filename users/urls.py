from django.urls import path
from . import views

urlpatterns=[
    path('',views.profiles,name="profiles"),
    path('userprofile/<str:pk>/',views.userprofile,name="userprofile"),
    
    path('loginpage/',views.loginpage,name="loginpage"),
    path('logoutpage/',views.logoutpage,name="logoutpage"),
    path('register/',views.registeruser,name="registerpage"),
    
    path('account/',views.useraccount,name="useraccount"),
    path('editaccount/',views.editaccount,name="editaccount"),
   
    path('create-skill/', views.createSkill, name="create-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
   
    path('inbox/',views.inbox,name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message")
]