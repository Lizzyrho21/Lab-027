from django.db import models
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

# create Snack model
# make sure it extends from proper base class
class Snack(models.Model):
    # making our variables available
    # add name as a CharField with maximum length of 64 characters.
    name = models.CharField(max_length=64)
    # add purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
    purchaser = models.ForeignKey(User, on_delete=models.CASCADE)
    # add description TextField
    description = models.TextField()





