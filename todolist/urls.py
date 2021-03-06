from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todolist/', views.list, name='list'),
    path('delete/<task_id>', views.delete_task, name='delete_task'),
    path('delete1/<query_id>', views.delete_query, name='delete_query'),
    path('edit/<task_id>', views.edit_task, name='edit_task'),
    path('complete/<task_id>', views.complete_task, name='complete_task'),
    path('pending/<task_id>', views.pending_task, name='pending_task'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')

]