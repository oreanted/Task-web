from django import forms
from .models import Task, Query


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task', 'done']


class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['email', 'query']