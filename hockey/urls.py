from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *
from .hotviews import *

# from competition.views import get_teams


urlpatterns = [
    path("hockey", Hotball, name="hockey"),
    # path("addtourn", addchampionship, name="addchampionship"),
    path("fixtures/", fixtures, name="hockey_fixtures"),
    path("futourn/<int:id>", hotourn_details, name="hockey_tournament"),
    path("hofixture/<int:id>", edit_hofixtures_view, name="update_hofixture"),
    path("fixturedetail/<int:id>", HoFixtureDetail, name="hofixture"),
    path("nstandings/", hockeyStandings, name="hockey_standings"),
    path(
        "generate_hofixtures/<int:id>/",
        generate_hofixtures_view,
        name="generate_hofixtures",
    ),
    # path("fixtures/", fixtures, name="fixtures"),
    path(
        "generate-next-round-fixtures/",
        generate_next_round_fixtures,
        name="generate_next_round_fixtures",
    ),
    # path("fixtures/", fixtures, name="fixtures"),
    path("addhofixtures/", create_hofixture, name="addhofixture"),
    # path("fixtures/", fixtures, name="fixtures"),
    path("Hockey/<int:id>", Hotbol, name="Hockey"),
    path("Hockey_fixtures", HoFixtures, name="Netfixtures"),
    path("hotfixtures/", hotfixtures, name="hotfixtures"),
    path("Hockey/", Hohome, name="Hockey"),
    path("Hockey_results", NResults, name="Netresults"),
    path("Netbalstandings", hobollStandings, name="Netstandings"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
