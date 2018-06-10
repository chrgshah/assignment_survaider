from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from users.controller import users

urlpatterns = [
    url(r'^$', users.index, name='index'),
    url(r'^get_records/$', users.get_records, name='get_records'),
    url(r'^get_distribution_gender/$', users.get_distribution_gender, name='get_distribution_gender'),
    url(r'^get_distribution_relationship/$', users.get_distribution_relationship, name='get_distribution_relationship')
]






