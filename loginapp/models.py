# from django.db import models
# from django.contrib.auth.models import AbstractUser, Permission, Group
#
# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('admin', 'Admin'),
#         ('client', 'Client'),
#     )
#     user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name='user permissions',
#         blank=True,
#         related_name='custom_user_permissions'  # Unique related_name
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name='groups',
#         blank=True,
#         related_name='custom_user_groups'  # Unique related_name
#     )


from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clients')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')

    def __str__(self):
        return self.user.username