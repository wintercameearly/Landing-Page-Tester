from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Traffic)
admin.site.register(Page)
admin.site.register(Speed)
admin.site.register(LinkCount)