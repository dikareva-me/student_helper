from django.db import models
from django.conf import settings


class Task(models.Model):
 # """Task model."""

  title = models.CharField(max_length=128, null=False)
  description = models.TextField(null=True, default=None, blank=True)
  subject = models.TextField(null=True, default=None, blank=True)
  is_complete = models.BooleanField(default=False)
  user = models.ForeignKey(                          
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name="task",
    null=True,
    blank=True
  )
  email = models.EmailField(null=True, default=None, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deadline = models.DateField()

  def __str__(self):
    return f"{self.user.first_name} - {self.title}"