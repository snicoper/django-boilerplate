from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    # /home/
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index'
    ),
]
