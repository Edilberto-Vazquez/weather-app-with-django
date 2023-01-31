from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import WeatherStation, WeatherRecord
import itertools


class IndexView(generic.ListView):
    template_name = "analysis/index.html"
    context_object_name = "station_list"

    def get_queryset(self):
        """Return all weather stations"""
        return WeatherStation.objects.all()


def line_chart_data_api(request: HttpRequest, station_id: int):
    weather_data = WeatherRecord.objects.filter(station_id=station_id).values()

    temp = {"label": "Temperature", "data": []}
    chill = {"label": "Chill", "data": []}
    dew = {"label": "Dew", "data": []}
    heat = {"label": "Heat", "data": []}
    hum = {"label": "Humidity", "data": []}
    bar = {"label": "Bar", "data": []}
    rain = {"label": "Rain", "data": []}
    for weather in weather_data:
        temp["data"].append(
            {
                "x": weather["record_date"].isoformat().split("T")[0],
                "y": weather["temp"],
            }
        )
        chill["data"].append(
            {
                "x": weather["record_date"].isoformat().split("T")[0],
                "y": weather["chill"],
            }
        )
        dew["data"].append(
            {"x": weather["record_date"].isoformat().split("T")[0], "y": weather["dew"]}
        )
        heat["data"].append(
            {
                "x": weather["record_date"].isoformat().split("T")[0],
                "y": weather["heat"],
            }
        )
        hum["data"].append(
            {"x": weather["record_date"].isoformat().split("T")[0], "y": weather["hum"]}
        )
        bar["data"].append(
            {"x": weather["record_date"].isoformat().split("T")[0], "y": weather["bar"]}
        )
        rain["data"].append(
            {
                "x": weather["record_date"].isoformat().split("T")[0],
                "y": weather["rain"],
            }
        )

    return JsonResponse(
        data={
            "datasets": [temp, chill, dew, heat, hum, bar, rain],
        }
    )


def graphic_detail(request: HttpRequest, station_id: int):
    return render(request, "analysis/graphic-detail.html", {"station_id": station_id})
