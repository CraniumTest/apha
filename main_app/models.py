from django.db import models

class HealthRecord(models.Model):
    user_id = models.IntegerField()
    record_date = models.DateField()
    medications = models.TextField()
    symptoms = models.TextField()
