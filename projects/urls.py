from django.urls import path
from . import views

urlpatterns=[
    path('',views.projects,name="projects"),
    path('project/<str:pk>/',views.project,name="project"),
    path('createproject/',views.createproject,name="createproject"),
    path('updateproject/<str:pk>/',views.updateproject,name="updateproject"),
    path('deleteproject/<str:pk>/',views.deleteproject,name="deleteproject"),
]