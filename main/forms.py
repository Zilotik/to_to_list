from .models import Tasks
from django.forms import TextInput, ModelForm, Textarea

class TasksForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'description']
        widgets = {
            'title': TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Что сделать'}),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Как сделать'}),
        }