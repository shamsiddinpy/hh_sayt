import random
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .froms import EmailForm
from .models import VerificationCode


class IndexView(TemplateView):
    template_name = 'apps/index.html'


class BlogView(TemplateView):
    template_name = 'apps/blog/blog.html'


def send_verification_code(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            verification_code = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            VerificationCode.objects.update_or_create(email=email, defaults={'code': verification_code})
            send_mail(
                'Verification Code',
                verification_code,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            # Store the email in the session
            request.session['email'] = email
            # Redirect to the login code form
            return redirect('login_code')
    else:
        form = EmailForm()

    return render(request, 'apps/register/register.html', {'form': form})


def login_code(request):
    email = request.session.get('email')
    if request.method == 'POST':
        code_entered = request.POST.get('code', '')
        verification_code = VerificationCode.objects.filter(email=email).first()
        if verification_code and code_entered == verification_code.code:
            del request.session['email']
            return redirect('blog')
        else:
            error_message = "Tasdiqlash kodi yaroqsiz. Iltimos, yana bir bor urinib ko'ring."
            return render(request, 'apps/register/register.html', {'error_message': error_message})
    return render(request, 'apps/register/register.html')
