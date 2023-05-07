from django import forms
from leads.models import Lead


class LeadForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',

        }
    ))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
            
        }
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'type': 'email',
            
        }
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            
        }
    ))
    class Meta:
        model = Lead
        fields = ['name', 'subject', 'email', 'message']
