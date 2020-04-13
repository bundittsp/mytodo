from django.db import models
from django import forms

# Create your models here.
class ToDoItem(models.Model):
    text = models.CharField(max_length=200)
    TYPES = (
        ('01', 'Important'),
        ('02', 'Normal'),
    )
    priority = models.CharField(max_length=2, choices=TYPES)
    complete_flag = models.BooleanField(default=False)
    display_order = models.IntegerField(default=99)
    create_date = models.DateTimeField(auto_now_add=True)


class ToDoItemModelForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ('text', 'priority', 'complete_flag')
