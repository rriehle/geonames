from django.db import models


class GeoNames(models.Model):

    class Meta:
        ordering = (
            'country_code',
            'postal_code',
        )
        verbose_name = 'GeoName'
        verbose_name_plural = 'GeoNames'

    country_code = models.CharField(
        "Country Code",
        max_length=2,
    )

    postal_code = models.CharField(
        "Postal Code",
        max_length=20,
    )

    place_name = models.CharField(
        "Place Name",
        max_length=180,
    )

    admin_name1 = models.CharField(
        "1st order subdivision (state) name",
        max_length=100,
    )

    admin_code1 = models.CharField(
        "1st order subdivision (state) code",
        max_length=20,
    )

    admin_name2 = models.CharField(
        "2nd order subdivision (county/province) name",
        max_length=100
    )

    admin_code2 = models.CharField(
        "2nd order subdivision (county/province) code",
        max_length=20,
    )

    admin_name3 = models.CharField(
        "3rd order subdivision (community) name",
        max_length=100
    )

    admin_code3 = models.CharField(
        "3rd order subdivision (community) code",
        max_length=20
    )

    latitude = models.FloatField(
        "estimated latitude (wgs84)",
    )

    longitude = models.FloatField(
        "estimated longitude (wgs84)",
    )

    accuracy = models.IntegerField(
        "accuracy of lat/lng from 0=missing then 1=estimated to 6=centroid",
        blank=True,
        default=0,
    )

    def __str__(self):
        return f'{self.country_code}-{self.postal_code}-{self.place_name}'
