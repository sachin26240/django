from django.db import models

# Create your models here.
class Food:
    id : int
    name : str
    desc : str
    img : str
    price : int