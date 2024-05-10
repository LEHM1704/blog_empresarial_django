from django import forms
from .models import NewsletterUser,Newsletter

class NewsLetterUserSignUpForm(forms.ModelForm):
    class Meta:
        model=NewsletterUser
        fields=['email']
        
class NewsLetterCreationForm(forms.ModelForm):
    class Meta:
        model=Newsletter
        fields=['name','subject','body','email','status']
        