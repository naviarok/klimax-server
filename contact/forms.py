from django import forms
from .models import Consultation, Message

CONSULTATION_METHOD_CHOICES = (
    ('video', 'Microsoft Teams meeting'),
    ('phone', 'Whatsapp Phone Call'),
    ('chat', 'Whatsapp Chat'),
)

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation

        fields = ['name', 'company', 'email', 'phone_number', 'description',
                  'current_website', 'date', 'time', 'consultation_method']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'Your name'}),
            'company': forms.TextInput(attrs={'class': 'bordered-box', 'placeholder':'Company name (optional)'}),
            'email': forms.EmailInput(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'Email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'bordered-box', 'placeholder':'Your phone number (optional)'}),
            'description': forms.Textarea(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'short description of your project'}),
            'current_website': forms.TextInput(attrs={'class': 'bordered-box', 'placeholder':'Your current website (optional)'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;', 'required':True}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;', 'required':True}),
            'consultation_method': forms.Select(choices=CONSULTATION_METHOD_CHOICES, attrs={'class': 'bordered-box', 'style': 'color: #ffffff; background-color: #000000;', 'required':True}),
        }

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message

        fields = ['name', 'subject', 'email', 'message']
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'Your name'}),
            'subject': forms.TextInput(attrs={'class': 'bordered-box','required':True, 'placeholder':'Subject'}),
            'email': forms.EmailInput(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'Email address'}),
            'message': forms.Textarea(attrs={'class': 'bordered-box', 'required':True, 'placeholder':'Your message'}),
        }