from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

CONDITION_CHOICES = (
    ('like new', 'Like new'),
    ('good', 'Good'),
    ('used', 'Used'),
)

YEAR_CHOICES = []
for r in range(1800, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class Product(models.Model):
    """
    A single product
    title, author, year of print, condition of book, provider, location,
    publisher, number of pages, price, summary, created_date, published_date,
    views, image
    """
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    year_of_edition = models.IntegerField(choices=YEAR_CHOICES,
                                          default=datetime.datetime.now().year)
    condition_of_book = models.CharField(max_length=10,
                                         choices=CONDITION_CHOICES,
                                         default='Like new')
    provider = models.ForeignKey(User, null=False, default=1, on_delete=models.SET_DEFAULT)
    location = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)
    number_of_pages = models.IntegerField(null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=00)
    summary = models.TextField(max_length=300, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True,
                                          default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", null=True)

    def __unicode__(self):
        return self.title
