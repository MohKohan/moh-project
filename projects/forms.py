from django.forms import ModelForm,widgets,MultiWidget, TextInput
from .models import *
from django import forms


class ProjectForm(ModelForm):
    required_css_class ='required-field'
    class Meta:
        model=Project
        fields= '__all__'
        exclude=['owner']
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
            }
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['project_image'].widget.attrs.update({'class':'form-control'})
        self.fields['used_links'].widget.attrs.update({'class':'form-control'})
        
        
# class RowProjectForm(forms.Form):
#     title=forms.CharField(widget=forms.TextInput(attrs=""))
#     description=forms.CharField(widget=forms.Textarea(attrs={"class":"input"}))
#     project_image=forms.ImageField()
          
        
    

        