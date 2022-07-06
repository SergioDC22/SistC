from django.contrib import admin
from .models import Cliente, Impuesto
# Register your models here.
admin.site.register(Impuesto)
admin.site.register(Cliente)