from django.contrib import admin

from .models import Task
from .models import User

admin.site.register(Task)
admin.site.register(User)
admin.site.site_header = 'Desafio Oh My Code'

# Register your models here.
