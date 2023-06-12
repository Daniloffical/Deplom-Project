from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_path', 'name', 'description', 'category', 'private', 'image']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"placeholder": "Введіть ім`я файлу"})
        self.fields['description'].widget.attrs.update({"placeholder": "Введіть опис файлу"})
