from django.db import models
from django.db.models.fields import CharField, SlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,db_index=True,unque=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
    def __str__(self):
        return self.name


