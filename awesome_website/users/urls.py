# from django.conf.urls import url
from users.views import dashboard
from django.urls import re_path

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
]

