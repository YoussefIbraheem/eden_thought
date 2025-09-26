from django.contrib import admin
from .models import Thought , Profile
from django.contrib.auth.models import User

admin.site.register(Thought)
admin.site.register(Profile)

