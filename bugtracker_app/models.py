from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    display_name = models.CharField(max_length=50, null=True, blank=True)

    REQUIRED_FIELDS = ['display_name']

    def __str__(self):
        return self.username
    

class BugTicket(models.Model):
    title = models.CharField(max_length=50)
    time_filed = models.DateTimeField(auto_now=False, auto_now_add=False)
    description = models.CharField(max_length=50)
    filed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='filed_by')
    STATUS_CHOICES = (
        ('NEW', 'New'),
        ('IN PROGRESS', 'In Progress'),
        ('DONE', 'Done'),
        ('INVALID', 'Invalid'),
    )
    ticket_status = models.CharField(max_length=11, choices=STATUS_CHOICES, default='NEW',)
    assigned_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='assigned_user')
    completed_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='completed_by')

    def __str__(self):
        return self.title
