from django.urls import path
from . import views

urlpatterns=[
path(r'',views.index,name='index'),
path(r'add',views.add),
path(r'view',views.view),
path(r'create',views.create,name='create'),
path(r'<int:id>/edit',views.edit),
path(r'<int:id>/update',views.update),
path(r'<int:id>/delete',views.delete),
path(r'about',views.about),
path(r'contact',views.contact),
]