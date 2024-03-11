from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a file', help_text='Only JPG and PDF files are allowed.', widget=forms.FileInput(attrs={'accept': 'image/jpeg,application/pdf'}))
