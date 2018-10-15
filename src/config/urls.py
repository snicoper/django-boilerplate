from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path
from django.views.static import serve

from home.views import IndexView

urlpatterns = [
    ##################################################
    # / Home page.
    re_path(r'^$', IndexView.as_view(), name='home_page'),
    ##################################################

    # /accounts/*
    re_path(r'^accounts/', include('accounts.urls')),

    # /auth/*
    re_path(r'^auth/', include('authentication.urls')),

    # /contact/*
    re_path(r'^contact/', include('contact.urls')),

    # /home/*
    re_path(r'^home/', include('home.urls')),

    # /pages/*
    re_path(r'^pages/', include('pages.urls')),

    # /admin/*
    re_path(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    import debug_toolbar

    urlpatterns += [
        re_path(r'^api-auth/', include('rest_framework.urls')),

        # /media/:<mixed>path/
        re_path(
            route=r'^media/(?P<path>.*)$',
            view=serve,
            kwargs={'document_root': settings.MEDIA_ROOT}
        ),

        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
