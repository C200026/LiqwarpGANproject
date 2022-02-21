from django import forms # Djangoが準備しているforms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm # 追加
from django.contrib.auth.models import User # 追加
from .models import ModelFile

class ImageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
    class Meta:
        model = ModelFile
        fields = ['image'] #, 'uploaded_at']

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
            

