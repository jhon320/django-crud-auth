"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tasks import views
from contacts import views as contact_views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Admin
    path('admin/', admin.site.urls),

    # Autenticación
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),

    # Tasks
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('create_task/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete/', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),

    # Contacts
    path('contacts/', contact_views.contacts, name='contacts'),
    path('create_contact/', contact_views.create_contact, name='create_contact'),
    path('contacts/<int:contact_id>/', contact_views.contact_detail, name='contact_detail'),
    path('contacts/<int:contact_id>/update/', contact_views.update_contact, name='update_contact'),
    path('contacts/<int:contact_id>/delete/', contact_views.delete_contact, name='delete_contact'),
]