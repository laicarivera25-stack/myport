from django.db import models

class Skills(models.Model):
    name = models.CharField(max_length=200)
    # Gidugangan nato og default=0 para dili mag-error kung blanko
    proficiency = models.IntegerField(default=0, help_text="Enter percentage (e.g. 85 for 85%)")

    def __str__(self):
        return self.name