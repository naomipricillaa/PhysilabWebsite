from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


from django.db import models
from django.contrib.auth.models import User

class CalculationHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='calculator_history')
    result = models.CharField(max_length=255)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.result}"