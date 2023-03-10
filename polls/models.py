from django.db import models

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
    category = models.ForeignKey(Category, 
    related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
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


