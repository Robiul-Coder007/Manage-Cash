from django.contrib import admin
from .models import *

admin.site.register(CustomUser)
admin.site.register(AddCash)
admin.site.register(Expense)