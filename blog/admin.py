from django.contrib import admin
from .models import POST
# Register your models here.
# admin.site.register(POST)
@admin.register(POST)
class show(admin.ModelAdmin):
    list_display = ['id','user','title','post']
    readonly_fields = ('date',)