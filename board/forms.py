from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
        

class NoticeForm(forms.ModelForm):
    
        
    
    class Meta:
        
        model = NoticeBoard

        fields = ['title','text',]

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'style': 'width: 66%', 'placeholder': '제목을 입력하세요.'}
                ),
                # 'author': forms.Select(
                #     attrs={'class': 'custom-select'},
                # ),
                'text' : forms.CharField(widget=CKEditorUploadingWidget()),



            }


class FreeForm(forms.ModelForm):
    
        
    
    class Meta:
        
        model = FreeBoard

        fields = ['title','text',]

        widgets = {
                'title': forms.TextInput(
                    attrs={'class': 'form-control', 'style': 'width: 66%', 'placeholder': '제목을 입력하세요.'}
                ),
                'text': forms.CharField(widget=CKEditorUploadingWidget()),

            }
