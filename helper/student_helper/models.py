from django.db import models
from django.conf import settings


class Task(models.Model):
 # """Task model."""

  title = models.CharField(max_length=128, null=False)
  description = models.TextField(null=True)
  subject = models.TextField(null=True)
  is_complete = models.BooleanField(default=False)
  user = models.ForeignKey(                           #used to define one-to-many relashionships
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="task",
    null=True,
    blank=True
  )
  email = models.EmailField(null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deadline = models.DateField()

  def __str__(self):
    return f"{self.user.first_name} - {self.title}"