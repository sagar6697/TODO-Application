from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  # Signup URL
    path('login/', views.login, name='login'),     # Login URL
    path('task_list/', views.task_list, name='task_list'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('update/<int:pk>/', views.update_task, name='update_task'),
]
