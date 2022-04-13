# from django.apps import AppConfig


# class MusicConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'Music'

from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class MusicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Music'
    # create path to models
    pass
