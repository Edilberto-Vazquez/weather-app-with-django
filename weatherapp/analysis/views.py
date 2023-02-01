from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.utils import timezone
from django.db.models.functions import Trunc
from django.db.models import Avg
from django.views import generic
from .models import WeatherStation, WeatherRecord
from datetime import datetime, timedelta


class IndexView(generic.ListView):
    template_name = "analysis/index.html"
    context_object_name = "station_list"

    def get_queryset(self):
        """Return all weather stations"""
        return WeatherStation.objects.all()


# template views
def get_time_labels(date_field: str, from_date: str, to_date: str) -> list:
    start = datetime.strptime(from_date, "%Y-%m-%d")
    end = datetime.strptime(to_date, "%Y-%m-%d")

    date_array = []

    while start <= end:
        if date_field == "month":
            date_array.append(start.strftime("%Y-%m"))
            start += timedelta(days=31)
        elif date_field == "year":
            date_array.append(start.year)
            start += timedelta(days=365)

    return list(dict.fromkeys(date_array)).sort()


def graphic_detail(request: HttpRequest, station_id: int, from_date: str, to_date: str):
    return render(
        request,
        "analysis/graphic-detail.html",
        {"station_id": station_id, "from_date": from_date, "to_date": to_date},
    )


# ednpoint views
def line_chart_data_api(
    request: HttpRequest, station_id: int, date_field: str, from_date: str, to_date: str
):
    labels = []
    temp = {"data": [], "label": "temp"}
    chill = {"data": [], "label": "chill"}
    dew = {"data": [], "label": "dew"}
    heat = {"data": [], "label": "heat"}
    hum = {"data": [], "label": "hum"}
    bar = {"data": [], "label": "bar"}
    rain = {"data": [], "label": "rain"}

    timeFormats = {"month": "%Y-%m", "year": "%Y"}

    """
        Example of the query with SQL
        SELECT DATE_TRUNC('day', analysis_weatherrecord.record_date) AS day,
        AVG(analysis_weatherrecord.temp) as temp
        FROM analysis_weatherrecord
        WHERE analysis_weatherrecord.station_id = 1
        GROUP  BY day
        ORDER  BY day;
    """

    from_date_formated = timezone.make_aware(datetime.strptime(from_date, "%Y-%m-%d"))
    to_date_formated = timezone.make_aware(datetime.strptime(to_date, "%Y-%m-%d"))

    weather_data = (
        WeatherRecord.objects.filter(
            station_id=station_id,
            record_date__range=(from_date_formated, to_date_formated),
        )
        .annotate(time=Trunc("record_date", date_field))
        .values("time")
        .annotate(
            temp=Avg("temp"),
            chill=Avg("chill"),
            dew=Avg("dew"),
            heat=Avg("heat"),
            hum=Avg("hum"),
            bar=Avg("bar"),
            rain=Avg("rain"),
        )
        .order_by("time")
    )

    for weather in weather_data:
        temp["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["temp"],
            }
        )
        chill["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["chill"],
            }
        )
        dew["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["dew"],
            }
        )
        heat["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["heat"],
            }
        )
        hum["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["hum"],
            }
        )
        bar["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["bar"],
            }
        )
        rain["data"].append(
            {
                "x": weather["time"].strftime(timeFormats[date_field]),
                "y": weather["rain"],
            }
        )

    labels = get_time_labels(date_field, from_date, to_date)

    return JsonResponse(
        data={
            "labels": labels,
            "datasets": [temp, chill, dew, heat, hum, bar, rain],
        }
    )
