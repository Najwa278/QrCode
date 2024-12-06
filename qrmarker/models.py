from django.db import models

# Create your models here.
from django.db import models

class QRCode(models.Model):
    data = models.TextField()
    logo_path = models.CharField(max_length=255, null=True, blank=True)
    color = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data

class QRScan(models.Model):
    qr_code = models.ForeignKey(QRCode, on_delete=models.CASCADE)
    device_info = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=50)
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scan of {self.qr_code.data} at {self.scanned_at}"