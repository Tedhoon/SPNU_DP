from django import forms
from .models import *



class ImageForm(forms.ModelForm):
    
        
    
    class Meta:
        
        model = ImageBoard

        fields = ['title', 'image', 'desc',]

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'style': 'width: 70%', 'placeholder': '제목을 입력하세요.'}
                ),
            
        }