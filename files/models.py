from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/', max_length=256)
    processed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
