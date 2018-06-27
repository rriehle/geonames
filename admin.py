from django.contrib import admin

from .models import GeoNames


class GeoNamesAdmin(
    # SalmonellaMixin,
    admin.ModelAdmin
):

    save_on_top = True

    list_display = (
        'country_code',
        'postal_code',
        'place_name',
        'admin_name1',
        'admin_code1',
        'admin_name2',
        'admin_code2',
        'admin_name3',
        'admin_code3',
        'latitude',
        'longitude',
        'accuracy',
    )

    list_filter = (
        'country_code',
    )

    search_fields = (
        'postal_code',
        'place_name',
    )

    # salmonella_fields = ()


admin.site.register(GeoNames, GeoNamesAdmin)