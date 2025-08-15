from django.db import models
from django.core.validators import RegexValidator

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10,15}$', 'Enter a valid phone number (10–15 digits)')])
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('service', 'date', 'time')

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"