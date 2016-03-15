from django.conf.urls import url
import users.views

urlpatterns =[
    url(r'^$', users.views.first_page),
    url(r'^login/', users.views.user_login),
    url(r'^logout/', users.views.user_logout),
	url(r'^register/', users.views.register),

]