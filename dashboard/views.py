from django.shortcuts import render, redirect
from accounts.models import Championship
from django.contrib import messages
from .forms import *
from django.http import HttpRequest, HttpResponse
from .models import *


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/dashboard.html")


# championships
def championships(request):
    championships = Championship.objects.all()
    context = {"championships": championships}
    return render(request, "dashboard/championships.html", context)


# add championships
def addchampionship(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ChampForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Championship added successfully.")
            return redirect("championships")
        else:
            messages.error(
                request,
                "There was an error in the form. Please correct it and try again.",
            )
    else:
        form = ChampForm()

    context = {"form": form}
    return render(request, "dashboard/newchamp.html", context)


def ChampDetail(request, id):
    championship = Championship.objects.get(id=id)

    seasons = Season.objects.filter(championship=championship)
    new_season = None

    if request.method == "POST":
        cform = SeasonForm(request.POST, request.FILES)

        if cform.is_valid():
            new_season = cform.save(commit=False)
            new_season.championship = championship

            new_season.save()
            return redirect("champDetail", championship.id)
    else:
        cform = SeasonForm()

    context = {
        "championship": championship,
        "seasons": seasons,
        "cform": cform,
    }

    return render(request, "dashboard/championship.html", context)


# championships
def teams(request):
    teams = SchoolTeam.objects.all()
    if request.method == "POST":
        form = SchoolTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "team added successfully.")
            return redirect("teams")
        else:
            messages.error(
                request,
                "There was an error in the form. Please correct it and try again.",
            )
    else:
        form = SchoolTeamForm()
    context = {"teams": teams, "form": form}
    return render(request, "teams/teams.html", context)


# add championships

from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404


def getTeamAthletes(request):
    school_id = request.GET.get("school")
    sport_id = request.GET.get("sports")
    gender = request.GET.get("genders")

    athletes = Athlete.objects.all()

    if school_id:
        athletes = athletes.filter(school_id=school_id)

    if sport_id:
        athletes = athletes.filter(sport_id=sport_id)

    if gender:
        athletes = athletes.filter(gender=gender)

    athletes_list = list(athletes.values("id", "fname", "lname"))

    data = {"athletes": athletes_list}

    return JsonResponse(data)


# add championships
# add championships
# add championships
def addteam(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SchoolTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "team added successfully.")
            return redirect("teams")
        else:
            messages.error(
                request,
                "There was an error in the form. Please correct it and try again.",
            )
    else:
        form = SchoolTeamForm()

    context = {"form": form}
    return render(request, "dashboard/newteam.html", context)


def TeamDetail(request, id):
    team = SchoolTeam.objects.get(id=id)

    new_athlete = None

    context = {
        "team": team,
    }

    return render(request, "teams/team.html", context)


# # @school_required
# def create_official(request):
#     # update school official


# officials list, tuple or array
def officials(request):
    officials = Official.objects.all()
    if request.method == "POST":
        form = OfficialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect("officials")
        else:
            # Attach errors to the form for display in the template
            error_message = "There was an error in the form submission. Please correct the errors below."
    else:
        form = OfficialForm()
    context = {"officials": officials, "form": form}
    return render(request, "officials/officials.html", context)


# view official details
def official_details(request, id):
    official = Official.objects.get(pk=id)

    return render(request, "officials/official.html", {"official": official})


# delete
def delete_official(request, id):
    official = Official.objects.get(id=id)
    return render(request, "officials/delete_official.html", {"official": official})
