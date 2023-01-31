from django.db import models


class WeatherStation(models.Model):
    location = models.CharField(max_length=50, verbose_name="place of operation")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    init_upload_date = models.DateTimeField(verbose_name="initial upload date")
    last_upload_date = models.DateTimeField(verbose_name="last upload date")
    active = models.BooleanField(verbose_name="station is active")
    name = models.CharField(max_length=50, verbose_name="station name")

    def __str__(self) -> str:
        return self.name


class WeatherRecord(models.Model):
    temp = models.FloatField(verbose_name="temperature")
    chill = models.FloatField(verbose_name="thermal sensation")
    dew = models.FloatField(verbose_name="dew point")
    heat = models.FloatField(verbose_name="heat")
    hum = models.FloatField(verbose_name="humidity")
    bar = models.FloatField(verbose_name="atmospheric pressure")
    rain = models.FloatField(verbose_name="rain")
    record_date = models.DateTimeField(verbose_name="registration date")
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)
