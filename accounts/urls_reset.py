from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^password-reset/$', auth_views.PasswordResetView.as_view(
        template_name='password_reset_form.html'),
        name='password_reset'),
    url(r'^password-reset-done/$', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html'),
        {'post_reset_redirect': reverse_lazy('password_reset_complete')},
        name='password_reset_confirm'),
    url(r'^password-reset-complete/$',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'),
        name='password_reset_complete'),
] 
