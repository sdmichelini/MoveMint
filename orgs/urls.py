from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^create/', views.create, name='create'),
		url(r'^(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})$', views.detail, name='detail'),
		url(r'^(?P<uuid>[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})/create/', views.create_project, name='create_project'),
]
