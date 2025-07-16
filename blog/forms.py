from django import forms
from website.models import Contact,Newsletter

class Contactform(forms.ModelForm):
    class Meta :
        model = Contact
        fields = "__all__"

class newsletterform(forms.ModelForm):
    class Meta :
        model = Newsletter
        fields = "__all__"
    
    