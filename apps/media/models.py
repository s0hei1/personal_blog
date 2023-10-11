from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=288, null=True, blank=True)
    image = models.ImageField(width_field='width', height_field='height', upload_to='images/')

    file_size = models.PositiveBigIntegerField(null=True, blank=True, editable=False)

    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)

    def save(self, *args, **kwargs):
        self.file_size = self.image.size
        super().save(*args, **kwargs)
