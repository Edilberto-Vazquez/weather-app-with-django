from django.test import TestCase, Client
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

    def test_line_chart_data_when_is_it_per_month_and_year(self):
        client = Client()
        expected_result_month = {
            "labels": ["2019-01"],
            "datasets": [
                {"data": [{"x": "2019-01", "y": 16.120338983050846}], "label": "temp"},
                {"data": [{"x": "2019-01", "y": 15.371186440677963}], "label": "chill"},
                {"data": [{"x": "2019-01", "y": 4.416949152542372}], "label": "dew"},
                {"data": [{"x": "2019-01", "y": 14.944067796610167}], "label": "heat"},
                {"data": [{"x": "2019-01", "y": 48.96610169491525}], "label": "hum"},
                {"data": [{"x": "2019-01", "y": 764.0050847457625}], "label": "bar"},
                {"data": [{"x": "2019-01", "y": 0.0}], "label": "rain"},
            ],
        }

        expected_result_year = {
            "labels": ["2019"],
            "datasets": [
                {"data": [{"x": "2019", "y": 16.120338983050846}], "label": "temp"},
                {"data": [{"x": "2019", "y": 15.371186440677963}], "label": "chill"},
                {"data": [{"x": "2019", "y": 4.416949152542372}], "label": "dew"},
                {"data": [{"x": "2019", "y": 14.944067796610167}], "label": "heat"},
                {"data": [{"x": "2019", "y": 48.96610169491525}], "label": "hum"},
                {"data": [{"x": "2019", "y": 764.0050847457625}], "label": "bar"},
                {"data": [{"x": "2019", "y": 0.0}], "label": "rain"},
            ],
        }

        # test when is month
        response_month = client.get(
            "/line-chart-data-api/1/month/2019-01-29/2019-01-30/"
        )
        self.assertEqual(response_month["content-type"], "application/json")
        self.assertEqual(response_month.status_code, 200)
        self.assertJSONEqual(
            str(response_month.content, encoding="utf8"), expected_result_month
        )

        # test when is year
        response_year = client.get("/line-chart-data-api/1/year/2019-01-29/2019-01-30/")
        self.assertEqual(response_year["content-type"], "application/json")
        self.assertEqual(response_year.status_code, 200)
        self.assertJSONEqual(
            str(response_year.content, encoding="utf8"), expected_result_year
        )
