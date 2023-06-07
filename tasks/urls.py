from django.urls import path
from . import views
app_name = 'tasks'
urlpatterns = [
    path('', views.index, name="index"),
    path('update/<int:pk>', views.updateTask, name="update"),
    path('delete/<int:pk>', views.deleteTask, name="delete"),
    path('deleteall/', views.deleteAll, name="deleteall"),
]
