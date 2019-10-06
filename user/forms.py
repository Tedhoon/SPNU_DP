from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label = 'password' , widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat_password' , widget = forms.PasswordInput)
    email = forms.EmailField(label=('Email'),required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'required': 'True',
        }
        )
        )
        # 이메일을 필수사항으로 받게 하기
    
        
    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email :
            if get_user_model().objects.filter(email=email).exists():
                raise forms.ValidationError('이미 사용중인 이메일 또는 인증되지 않은 이메일입니다.')
        return email
        # 중복 이메일 못받게 하기

    class Meta :
        model = User 
        fields = ['username', 'email']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('두 비밀번호가 다릅니다.')
        return cd['password2']

    
    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if username :
            if get_user_model().objects.filter(username=username).exists():
                raise forms.ValidationError('해당 ID가 존재하거나 인증되지 않은 유저입니다. 가입시 입력한 이메일을 확인하세요.')
        return username
