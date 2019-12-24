from django.db import models


class Package(models.Model):
    ACCEPTED = 'AC'
    TRANSIT = 'TR'
    DELIVERED = "DV"
    REJECTED = "RJ"

    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (TRANSIT, 'In transit'),
        (DELIVERED, 'Delivered'),
        (REJECTED, 'Rejected'),
    ]

    sender_name = models.CharField(max_length=255)
    receiver_name = models.CharField(max_length=255)
    tracking_number = models.CharField(max_length=255)
    address_from = models.CharField(max_length=255)
    address_to = models.CharField(max_length=255)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2, default=ACCEPTED)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.FloatField(default=0)
    accepted_at = models.DateTimeField(auto_now=True)
    delivered_at = models.DateTimeField(null=True)
