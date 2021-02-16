from django.db import models

# Create your models here.

class Notes(models.Model):
    task_title = models.CharField("Task_Title", max_length=255)
    description = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)

    def __str__(self):
        return self.first_name