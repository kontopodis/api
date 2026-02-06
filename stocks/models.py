from django.db import models
import uuid
# Create your models here.
class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    ticker = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"

