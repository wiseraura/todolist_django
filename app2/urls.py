from django.urls import path
from . import views

urlpatterns = [
    path("", views.user_list),
    path("tasks/", views.task_list),
    path("task/<int:task_id>/", views.task_detail),
    path("create_task/", views.create_task, name='create_task'),
]
