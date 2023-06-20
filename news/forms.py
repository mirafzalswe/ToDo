from .models import Todo
from django.forms import ModelForm, TextInput, DateInput, Textarea


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['name_task', 'task_txt', 'date']

        widgets = {
            'name_task': TextInput(attrs={
                'class': 'form-control',
                'placeholder' : "name task"
            }),
            'task_txt': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "task"
            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'data-time'
            })
        }
