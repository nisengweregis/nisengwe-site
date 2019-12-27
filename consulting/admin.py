from django.contrib import admin

# Register your models here.

from .models import Consulting


class ConsultingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


admin.site.register(Consulting, ConsultingAdmin)
