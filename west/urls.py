from django.conf.urls import url
import west.views

urlpatterns = [
    url(r'^$', west.views.first_page),
    url(r'^staff/',west.views.staff),
    url(r'^templay/',west.views.templay),
    url(r'^inherit/',west.views.inherit),
    url(r'^form/',west.views.form),
    url(r'^investigate/',west.views.investigate),
    url(r'^investigates/',west.views.investigates),

]