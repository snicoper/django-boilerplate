from django.urls import path, re_path

from . import views

app_name = 'contact'

urlpatterns = [

    # /contact/
    path(
        route='',
        view=views.ContactView.as_view(),
        name='contact'
    ),

    # /contact/list/
    path(
        route='list/',
        view=views.ContactListView.as_view(),
        name='list'
    ),

    # /contact/details/
    re_path(
        route=r'^details/(?P<pk>\d+)/$',
        view=views.ContactDetailView.as_view(),
        name='details'
    ),

    # /contact/delete/
    re_path(
        route=r'^delete/(?P<pk>\d+)/$',
        view=views.ContactDeleteView.as_view(),
        name='delete'
    ),
]
