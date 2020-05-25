from django import forms
from bugtracker_app.models import CustomUser

class LogInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    display_name = forms.CharField(max_length=40)

STATUS_CHOICES = (
    ('NEW', 'New'),
    ('IN PROGRESS', 'In Progress'),
    ('DONE', 'Done'),
    ('INVALID', 'Invalid'),
)

class BugTicketForm(forms.Form):
    title = forms.CharField(max_length=50)
    time_filed = forms.DateTimeField()
    filed_by = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    ticket_status = forms.ChoiceField(choices=[STATUS_CHOICES], required=False)
    assigned_user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
    completed_by = forms.ModelChoiceField(queryset=CustomUser.objects.all())

    def __str__(self):
        return self.title
