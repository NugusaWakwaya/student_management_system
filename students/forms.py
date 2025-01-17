from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields =['student_number','first_name','last_name','email','field_of_study', 'GPA']
        labels = {
            'student_number':'student Number',
            'first_name':'first Name',
            'last_name':'last Name',
            'email':'Email',
            'field_of_study':'Field of study',
            'GPA':'GPA'
            
        }
        widgets = {
            'student_number':forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'field_of_study':forms.TextInput(attrs={'class':'form-control'}), 
            'GPA':forms.NumberInput(attrs={'class':'form-control'})

        }
