from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['id', ]
    # list_display = ['id']

admin.site.register(Profile, ProfileAdmin)