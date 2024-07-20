from django.db import models

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    publish_date = models.DateField()  # Asegúrate de que este campo esté definido si lo estás usando

    def _str_(self):
        return self.title




















