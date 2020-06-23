from django import forms
from bugtracker_app.models import CustomUser

class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=40)

STATUS_CHOICES = [
    ('NEW', 'New'),
    ('IN PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
    ('INVALID', 'Invalid'),
]

class BugTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=50)

    def __str__(self):
        return self.title
