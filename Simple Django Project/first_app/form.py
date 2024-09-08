from django import forms
from django.core import validators
from first_app.models import FormData


# To connect the form to the model and the database,
# use 'forms.ModelForm', not 'forms.Form'.
# Cutom validations can be added.
class NewForm(forms.ModelForm):

    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    
    class Meta():
        model = FormData   # Connecting the form to the model
        fields = '__all__'


# My Validator Parameter
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError('Name must start with letter "z"!')


# class MyForm(forms.Form):
#
#     # name = forms.CharField(validators=[check_for_z)
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter email again:')
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False,
#     #                             widget=forms.HiddenInput,
#     #                             validators=[validators.MaxLengthValidator(0)])
#
#     # My Validator/Clean Method
#     # Django naming convention for validation methods
#     # def clean_botcatcher(self):
#     #     botcatcher = self.cleaned_data['botcatcher']
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError('Gotcha Bot!!!')
#     #     return botcatcher
#
#     # Validate the entire form at once
#     # We can also add other form fields here for validation.
#     def clean(self):
#         all_cleaned_data = super().clean()
#         email = all_cleaned_data['email']
#         vmail = all_cleaned_data['verify_email']
#
#         if email != vmail:
#             raise forms.ValidationError("Emails don't match!")
