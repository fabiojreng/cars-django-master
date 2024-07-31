from django.contrib import admin
from cars.models import Car, Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "brand",
        "factory_year",
        "model_year",
        "value",
        "created_at",
        "updated_at",
    )
    search_fields = ("model", "value")


admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)
