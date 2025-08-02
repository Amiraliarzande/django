from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html', success_url=reverse_lazy('accounts:password_reset_done')), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', success_url=reverse_lazy('accounts:password_reset_complete')), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name="password_reset_complete"),
]