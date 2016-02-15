from django import forms


class UploadForm(forms.Form):
    upload_data = forms.FileField(label=False)