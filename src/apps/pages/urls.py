from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    # Cookies Consent
    path(
        route='cookie-consent/',
        view=views.CookieConsentView.as_view(),
        name='cookie_consent'
    ),

    # About
    path(
        route='about/',
        view=views.AboutView.as_view(),
        name='about'
    ),
]
