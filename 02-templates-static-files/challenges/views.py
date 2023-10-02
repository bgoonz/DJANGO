from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Read a book for 15 minutes every day!",
    "may": "Drink 8 glasses of water daily!",
    "june": "Practice meditation for 10 minutes every day!",
    "july": "No sugary drinks for the entire month!",
    "august": "Write a journal entry every day!",
    "september": "Learn a new language for 20 minutes daily!",
    "october": "Exercise for at least 30 minutes every day!",
    "november": "Limit screen time to 2 hours daily outside of work/school!",
    "december": "Volunteer or do a good deed daily!",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month.capitalize()},
        )
    except KeyError:
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")
