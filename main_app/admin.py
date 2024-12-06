from django.contrib import admin
from .models import Cat, Feeding

admin.site.register(Cat)

# Register the new Feeding model
admin.site.register(Feeding)