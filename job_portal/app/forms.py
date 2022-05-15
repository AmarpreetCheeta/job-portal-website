from tkinter.messagebox import NO
from django import forms
from app.models import *
from django.contrib.auth.forms import *


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(
        attrs={'placeholder':'Enter your password'}
    ))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(
        attrs={'placeholder':'Confirm your password'}
    ))
    
    class Meta:
        model = UserAccount
        fields = ['first_name','username','email','phone','state','gender']
        widgets = {
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your full name'}),
            'username':forms.TextInput(attrs={'placeholder':'Enter your username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email address','autocomplete':'off'}),
            'phone':forms.NumberInput(attrs={'placeholder':'Enter your phone number'}),
            'state':forms.Select(),
            'gender':forms.Select(),
        }
        
    def __init__(self,*args, **kwargs):
        super(SignUpForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs.pop('autofocus',None)
        
        
        
class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder':'Email Address'}
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder':'Password', 'class':'show form-control'}
    ))
    
    
    
class ResumeSubmitForm(forms.ModelForm):
    class Meta:
        model = ResumeSubmitModel
        fields = ['full_name','email','phone','location','linked_in','education','higher_education',
        'skills','project','birth_date','nationality','hobbies','address','objectives','declaration']
        widgets = {
            'full_name' :forms.TextInput(),
            'email' :forms.EmailInput(),
            'phone' :forms.NumberInput(),
            'location' :forms.TextInput(),
            'linked_in' :forms.URLInput(),
            'education' :forms.Textarea(),
            'higher_education' :forms.Textarea(),
            'skills' :forms.Textarea(),
            'project' :forms.Textarea(),
            'birth_date' :forms.DateInput(attrs={'type':'date'}),
            'nationality' :forms.Select(),
            'hobbies' :forms.Textarea(),
            'address' :forms.Textarea(),
            'objectives' :forms.Textarea(attrs={'class':'_text_area_input'}),
            'declaration' :forms.Textarea(attrs={'class':'_text_area_input'}),
        }
        
        
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = ['company_name','industry_type','headquarter','city','email','phone','start_date','logo',
        'discription']
        widgets = {
            'company_name':forms.TextInput(),
            'industry_type':forms.TextInput(),
            'headquarter':forms.TextInput(),
            'city':forms.Select(),
            'email':forms.EmailInput(),
            'phone':forms.NumberInput(),
            'start_date':forms.DateInput(attrs={'type':'date'}),
            'logo':forms.FileInput(attrs={'class':'img_iput form-control'}),
            'discription':forms.Textarea(),
        }
        
        

class SubmitJobsForms(forms.ModelForm):
    class Meta:
        model = SubmitJobsModel
        fields = ['job_title','location','email','company_name','salary','job_type','skills','discription']
        widgets = {
            'job_title':forms.TextInput(),
            'location':forms.TextInput(),
            'email':forms.EmailInput(),
            'company_name':forms.Select(),
            'salary':forms.NumberInput(),
            'job_type':forms.Select(),
            'skills':forms.Textarea(),
            'discription':forms.Textarea(),
        }
        
        
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name','email','message']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder':'Enter your full name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email'}),
            'message':forms.Textarea(attrs={'placeholder':'Write your message...','class':'_msg_hy'}),
        }
        
        
        
class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = UserAccount
        fields = ['image','first_name','username','email','phone','state','gender']
        widgets = {
            'image':forms.FileInput(attrs={'class':'img_input'}),
            'first_name':forms.TextInput(),
            'username':forms.TextInput(),
            'email':forms.EmailInput(attrs={'autocomplete':'off'}),
            'phone':forms.NumberInput(),
            'state':forms.Select(),
            'gender':forms.Select(),
        }
        
        

class PasswordUpdateForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())