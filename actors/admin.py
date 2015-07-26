from django.contrib import admin
from .models import (
		SubZone,
		Category,
		Amendity
		)
admin.site.register(SubZone)
admin.site.register(Category)
admin.site.register(Amendity)