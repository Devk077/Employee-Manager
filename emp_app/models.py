from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    lname = models.CharField(max_length=100)
    lid = models.CharField(max_length=100)

    def __str__(self):
        return self.lname


class Department(models.Model):
    dname = models.CharField(max_length=100)
    did = models.CharField(max_length=100)
    dlocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.dname


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    edept = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug = AutoSlugField(unique=True, populate_from='eid')

    def get_absolute_url(self):
        return reverse("emp_app:employee_details", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.ename
