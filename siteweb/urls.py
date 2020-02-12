from django.conf.urls import url
from .views import (
    login_view,
    register_view,
    logout_view,
    user_update,
)

urlpatterns = [
    url(r"^login/$", login_view, name = "login"),
]

urlpatterns += [
    url(r"^register/$", register_view, name = "register"),
]

urlpatterns += [
    url(r'^logout/$', logout_view, name = "logout"),
]

urlpatterns += [
	url(r'^(?P<pk>\d+)/update/$', user_update, name='userupdate'),
]