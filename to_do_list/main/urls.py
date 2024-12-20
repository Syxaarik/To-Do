from django.urls import path
from .views import index, edit, delete

urlpatterns = [
    path('', index, name='home'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:task_id>/', delete, name='delete_task'),

]
