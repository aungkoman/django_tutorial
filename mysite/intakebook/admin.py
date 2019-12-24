from django.contrib import admin
from .models import McType, Rank, Academy, Role, Soldier
# Register your models here.

admin.site.register(McType)
admin.site.register(Rank)
admin.site.register(Academy)
admin.site.register(Role)
admin.site.register(Soldier)
