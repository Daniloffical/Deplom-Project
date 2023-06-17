from django import forms
from .models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['file_path', 'name', 'description', 'private', 'image']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user','')
        category = kwargs.pop('category','')
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({"placeholder": "Введіть ім`я файлу"})
        self.fields['description'].widget.attrs.update({"placeholder": "Введіть опис файлу"})
        self.fields['name'].widget.attrs.update({"required": "required"})
        self.fields['description'].widget.attrs.update({"required": "required"})