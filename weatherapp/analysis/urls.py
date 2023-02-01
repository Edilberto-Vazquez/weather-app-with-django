from django.urls import path

from . import views

app_name = "analysis"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "graphic-detail/<int:station_id>/<str:from_date>/<str:to_date>/",
        views.graphic_detail,
        name="graphic-detail",
    ),
    path(
        "line-chart-data-api/<int:station_id>/<str:date_field>/<str:from_date>/<str:to_date>/",
        views.line_chart_data_api,
        name="line-chart-data-api",
    ),
]
