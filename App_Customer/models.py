from django.db import models

# Create your models here.


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=264, verbose_name='Customer Name')
    address = models.CharField(max_length=264, verbose_name='Customer Address')
    contact = models.CharField(max_length=264, verbose_name='Customer Phone Number')
    email = models.EmailField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name

