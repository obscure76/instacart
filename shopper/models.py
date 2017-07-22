from django.db import models
from django.utils import timezone

# Create your models here.


class Applicant(models.Model):
    """
    Model for Applicant
    """
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    phone_type = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    over_21 = models.BooleanField(default=False)
    reason = models.TextField()
    workflow_state = models.CharField(max_length=100)
    created_at = models.DateTimeField(db_index=True, default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.id, self.first_name, self.last_name,
                                      self.email, self.phone, self.workflow_state)
