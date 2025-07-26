from django import forms
from website.models import Contact,Newsletter
from blog.models import Comment
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post','name', 'email','subject', 'message']
        
    