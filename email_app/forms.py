from django import forms

CONVERT_OPTIONS = [
    ('html', 'HTML only'),
    ('html_pdf', 'HTML + PDF'),
    ('html_png', 'HTML + PNG'),
    ('html_jpg', 'HTML + JPG'),
]

SENDING_METHOD_CHOICES = [
    ('smtp', 'SMTP'),
    ('google_api', 'Google API'),
]

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class EmailForm(forms.Form):
    conversion_type = forms.ChoiceField(choices=CONVERT_OPTIONS)
    sending_method = forms.ChoiceField(choices=SENDING_METHOD_CHOICES)


class FileUploadForm(forms.Form):
    contacts_file = forms.FileField(label='Upload contacts.csv', required=False)
    subjects_file = forms.FileField(label='Upload subjects.csv', required=False)
    gmail_file = forms.FileField(label='Upload gmail.csv', required=False)
    html_file = forms.FileField(label='Upload send_code.html', required=False)

class CredentialsUploadForm(forms.Form):
    accounts_file = forms.FileField(label='Upload accounts.csv', required=False)
    credentials_files = MultipleFileField(label='Select files', required=False)
