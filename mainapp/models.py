from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(BaseModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(BaseModel):
    image = models.ImageField(upload_to='category/', blank=True, null=True)

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return "Image is not defined"


class Product(BaseModel):
    size = models.IntegerField(null=True)
    manfacturer = models.CharField(max_length=100, null=True)
    theory = models.IntegerField(null=True)
    unit = models.CharField(max_length=20, null=True)
    price_cash = models.IntegerField(null=True)
    price_cashless = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)


class Technicians(models.Model):
    full_name = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



