from django.contrib.auth.models import User
from django.forms import ModelForm


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
