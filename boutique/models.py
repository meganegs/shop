from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)


class Livreur(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    date_de_naissance = models.CharField(max_length=200, db_index=True)
    date_inscription = models.CharField(max_length=200, db_index=True)
    postal_addresse = models.CharField(max_length=200, db_index=True)
    adresse_facturation = models.CharField(max_length=200)
    email = models.CharField(max_length=200, db_index=True)
    password = models.CharField(max_length=50)

class Login(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    prenoms = models.CharField(max_length=200, db_index=True)
    email = models.CharField(max_length=200, db_index=True)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)

    #class Meta:
    #    odering = ('name',)
    #    verdose_name = 'category'
    #    verdose_name_plural = 'categories'
    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse('boutique:', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0.0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='products', blank=True, null=True)
    category = models.ForeignKey(Category, 
    related_name='products', on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%d', blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def  __str__(self):
        return self.name

    def gt_absolute_url(self):
        return reverse('boutique:', args=[self.id, self.slug])


