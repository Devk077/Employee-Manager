import os
import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "emp_management_system.settings")
django.setup()

from emp_app.models import Location, Department, Employee

fake = Faker()

# Create fake locations
for _ in range(5):
    Location.objects.create(
        lname=fake.city(),
        lid=fake.uuid4(),  # Using Faker's uuid4 method for simplicity
    )

# Create fake departments
for _ in range(10):
    Department.objects.create(
        dname=fake.company(),
        did=fake.uuid4(),
        dlocation=Location.objects.order_by('?').first(),
    )

# Create fake employees
for _ in range(50):
    Employee.objects.create(
        eid=fake.uuid4(),
        ename=fake.name(),
        eemail=fake.email(),
        econtact=fake.phone_number(),
        edept=Department.objects.order_by('?').first(),
    )

print("Population completed!")
