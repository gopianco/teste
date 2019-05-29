from django.db import models
from django.utils import timezone

shippng_method = (
    ('0414', 'SEDEX'),
    ( '04510', 'PAC'),
    ('0215', 'SEDEX10'),
)

class Purchase(models.Model):
    purchase_id = models.AutoField(primary_key=True)
    purchase_data = models.DateTimeField(default = timezone.now)
    tracking_code = models.CharField(max_length = 200)
    purchase_amount = models.CharField(max_length = 200)
    tracking_mode = models.CharField(max_length = 6, choices=shippng_method)
    shippng_time = models.CharField(max_length = 2)
    
    def save_purchase(self):
        self.save()
        
