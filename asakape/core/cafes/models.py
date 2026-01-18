from django.db import models

class Tags(models.Model):
    aesthetic = models.CharField(max_length=20, blank=True)
    specialty = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.specialty

class Cafe(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20, blank=True)
    location_x = models.DecimalField(max_digits=9, decimal_places=6)
    location_y = models.DecimalField(max_digits=9, decimal_places=6)
    thumbnail = models.ImageField(upload_to='cafe_photos/', null=True, blank=True)

    PRICE_CHOICES = [
        (1, '0-100'),
        (2, '100-200'),
        (3, '200-300'),
        (4, '300+')
    ]

    price_level = models.IntegerField(
        choices=PRICE_CHOICES,
        default=1
    )

    atmosphere = models.CharField(max_length=10, blank=True)

    WIFI_OPTIONS = [
        (1, 'None'),
        (2, 'Voucher'),
        (3, 'Unli')
    ]
    wifi_type = models.IntegerField(
        choices=WIFI_OPTIONS,
        default=1
    )
    
    socket_availability = models.BooleanField()
    is_24_7 = models.BooleanField()

    raw_hours = models.CharField(max_length=100, blank=True) #raw data for scraping.
    open_time = models.TimeField(null=True, blank=True) #null=true because it cannot be an empty string
    close_time = models.TimeField(null=True, blank=True)

    tags = models.ManyToManyField(Tags, blank=True, related_name='cafes')    

    def __str__(self):
        return self.name
