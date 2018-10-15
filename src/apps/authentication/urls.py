from django.urls import path, re_path

from . import views

app_name = 'authentication'

urlpatterns = [
    # Muestra el formulario de registro.
    path(
        route='register/',
        view=views.RegisterUserFormView.as_view(),
        name='register'
    ),

    # El registro ha sido satisfactorio.
    path(
        route='register/success/',
        view=views.RegisterUserSuccessView.as_view(),
        name='success'
    ),

    # Valida un token.
    re_path(
        route=r'^register/validate/(?P<token>[a-zA-Z0-9]{32})/$',
        view=views.RegisterUserValidateTokenView.as_view(),
        name='validate_token'
    ),

    # Formulario login.
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),

    # Logout.
    re_path(
        route=r'^logout/$',
        view=views.LogoutView.as_view(),
        name='logout'
    ),

    # Formulario cambiar contraseña.
    path(
        route='password-change/',
        view=views.PasswordChangeView.as_view(),
        name='password_change'
    ),

    # Muestra mensaje cambio password ok.
    path(
        route='password-change/done/',
        view=views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # Restablecer contraseña (Contraseña olvidada).
    path(
        route='password-reset/',
        view=views.PasswordResetView.as_view(),
        name='password_reset'
    ),

    # Informa al usuario que se ha mandado un email para restablecer la contraseña.
    path(
        route='password-reset/done/',
        view=views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),

    # Verifica el token, se accede desde el email.
    # Si es correcto, mostrara un formulario para crear nueva contraseña.
    re_path(
        route=(
            r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/'
            r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$'
        ),
        view=views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),

    # El token se ha verificado y muestra el resultado.
    path(
        route='reset/done/',
        view=views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    # Actualizar el email.
    path(
        route='email/update/',
        view=views.UserEmailUpdateView.as_view(),
        name='email_update'
    ),

    # Validación del token para cambiar el email.
    re_path(
        route=r'^email/validate/(?P<token>[\w]{30})/$',
        view=views.UserEmailUpdateValidateView.as_view(),
        name='email_update_validate'
    ),

    # Token para cambiar email no existe.
    path(
        route='token/error/',
        view=views.UserEmailUpdateNotFoundView.as_view(),
        name='token_email_not_exists'
    ),

    # Eliminar email temporal por parte del usuario.
    path(
        route='email-temporal/remove/',
        view=views.UserRemoveEmailUpdateView.as_view(),
        name='user_remove_email_temporal'
    ),
]
