from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    ine = models.CharField(max_length=20, null=False)
    rfc = models.CharField(max_length=15, null=False)
    nss = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=45, null=False)
    password = models.CharField(max_length=10, null=False)
    status = models.BooleanField(null=False)
    date_start = models.DateTimeField(null=False)

class Payroll(models.Model):
    id_payroll = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE,null=False)
    payment_date = models.DateField(null=False)

class Roles(models.Model):
    id_roles = models.AutoField(primary_key=True)
    rol_name = models.CharField(max_length=50, null=False)