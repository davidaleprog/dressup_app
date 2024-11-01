from django.db import models

# Create your models here.
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='media/images/')  # Requires Pillow library

    #optionnal fields
    color = models.CharField(max_length=50, null=True, blank=True)
    shape = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items_db'

    def __str__(self):
        return f"{self.type} - {self.color} - {self.shape}"

class Outfit(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    items = models.ManyToManyField(Item, related_name='outfits')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'outfits_db'

    def __str__(self):
        return self.name