from django.urls import path

from apps.views import send_verification_code, IndexView, login_code, BlogView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('send-email/', send_verification_code, name='register'),
    path('login-code/', login_code, name='login_code')
]
