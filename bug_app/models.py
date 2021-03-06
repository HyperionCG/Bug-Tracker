from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    pass


class Ticket(models.Model):
    New = 'New'
    In_Progress = 'In Progress'
    Invalid = 'Invalid'
    Done = 'Done'

    title = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=200)
    filer = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='filer',
        blank=True,
        null=True
    )
    assigned = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='assigned',
        blank=True,
        null=True
    )
    completed = models.ForeignKey(
        MyUser,
        on_delete=models.CASCADE,
        related_name='completed',
        blank=True,
        null=True
    )
    STATUS_CHOICES = [
      (New, 'New'),
      (In_Progress, 'In Progress'),
      (Done, 'Done'),
      (Invalid, 'Invalid'),  
    ]
    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=New)

    def __str__(self):
        return self.title