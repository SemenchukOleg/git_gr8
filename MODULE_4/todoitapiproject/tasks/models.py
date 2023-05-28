from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICE = (
        "No priority",
        "Low",
        "Medium",
        "High",
        )
    PRIORITY_CHOICE = tuple(zip(PRIORITY_CHOICE, PRIORITY_CHOICE))
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=200, blank=False)
    priority = models.CharField(choices=PRIORITY_CHOICE, max_length=15, default=PRIORITY_CHOICE[0][0])
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,blank=False , on_delete=models.CASCADE, null=False)

    @property
    def short_description(self):
        return self.description[:20] + '...'
    
    @classmethod
    def get_priorities_list(self):
        return[priority[0] for priority in self.PRIORITY_CHOICE]

    class Meta:
        ordering = ['-updated_at']