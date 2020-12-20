#J created the urls.py file which holds the url details of various pages in our project.
#J added three paths
#J 1. "" - main page which will showcase all the projects that are created.
#J 2. 'add' - which will let us add the new project(it's the callable route view which takes request and return response).
#J 3. '<slug:project_slug>' -dynamic route created when new project gets added.



from django.urls import path
from django.contrib import admin
from . import views

#urls required
urlpatterns = [
    path('', views.project_list, name='list'),
    path('add', views.ProjectCreateView.as_view(), name='add'),
    path('<slug:project_slug>', views.project_detail, name='detail')
]