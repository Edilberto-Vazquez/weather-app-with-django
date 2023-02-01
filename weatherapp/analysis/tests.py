from django.test import TestCase
from .models import WeatherStation


class WeatherRecordModelTest(TestCase):
    def test_weather_stations_list(self):
        """weather stations list return a list with the stations"""
        expected_result = [
            {"id": 1, "name": "INAOE"},
            {"id": 2, "name": "GTM-SIERRA-NEGRA"},
            {"id": 3, "name": "BUAP-CRC"},
            {"id": 4, "name": "UPAEP-PUE"},
            {"id": 5, "name": "ITP"},
            {"id": 6, "name": "COATZACOALCOS"},
        ]
        weather_stations = list(WeatherStation.objects.all().values("name", "id"))
        self.assertEqual(weather_stations, expected_result)
