from django.conf.urls import url

from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
		url(r'^login/', views.login_view, name='login'),
		url(r'^logout/', views.logout_view, name='logout'),
		url(r'^signup/regions', views.signup_regions, name='regions'),
		url(r'^signup/issues', views.signup_issues, name='issues'),
		url(r'^signup/', views.signup, name='signup'),

]
