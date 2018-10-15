from django.urls import path, re_path

from . import views

app_name = 'accounts'

urlpatterns = [
    # Perfil de usuario
    path(
        route='profile/',
        view=views.IndexView.as_view(),
        name='profile'
    ),

    # Editar photo usuario
    re_path(
        route=r'^profile/photo-update/(?P<slug>[\w\-]+)/$',
        view=views.PhotoUpdateView.as_view(),
        name='photo_update'
    ),
]
