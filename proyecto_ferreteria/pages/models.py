from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Nuevo campo para la imagen

    def __str__(self):
        return self.title





















