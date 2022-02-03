from django.db import models

from django.conf import settings

# Image upload Function

def upload_status_image(instance ,filename):
    return "uploads/{user}/{filename}".format(user=instance.user, filename=filename)

# Create your models here.
class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(null=True, blank=True, max_length=500)
    image = models.ImageField(upload_to=upload_status_image, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.content)[0:30]

    class Meta:
        verbose_name_plural = 'Status list'
