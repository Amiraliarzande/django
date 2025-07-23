from django import forms
from website.models import Contact,Newsletter
from captcha.fields import CaptchaField

class Contactform(forms.ModelForm):
    captcha = CaptchaField()  # Adding captcha field for spam protection
    class Meta :
        model = Contact
        fields = "__all__"

class newsletterform(forms.ModelForm):
    class Meta :
        model = Newsletter
        fields = "__all__"
    
    