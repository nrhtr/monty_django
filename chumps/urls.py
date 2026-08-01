from django.urls import path
from . import views

urlpatterns = [
    # home / 2010
    path("", views.index, name="index"),
    # api
    path("api/chumps/", views.chumps_api, name="chumps_api"),
    path("api/timeline.json", views.timeline_json, name="timeline_json"),
    # 1990
    path("1990/", views.index_1990, name="index_1990"),
    path("1990/entry/", views.entry_1990, name="entry_1990"),
    path("1990/history/", views.history, name="history"),
    path("1990/stats/", views.stats, name="stats"),
    path("1990/cool_pix/", views.cool_pix, name="cool_pix"),
    path("1990/wpaper/", views.wpaper, name="wpaper"),
    path("1990/mycats/", views.mycats, name="mycats"),
    # 2000
    path("2000/", views.index_2000, name="index_2000"),
    path("2000/about/", views.about_2000, name="about_2000"),
    path("2000/history/", views.history_2000, name="history_2000"),
    path("2000/stats/", views.stats_2000, name="stats_2000"),
]
