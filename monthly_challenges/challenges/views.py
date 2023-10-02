from django.shortcuts import render
from django.http import (
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
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
        response_data = f"<h1 style=\"color:blue\">{challenge_text}</h1>"
    except KeyError:
        return HttpResponseNotFound("<h2>This month is not supported!</h2>")
    else:
        return HttpResponse(response_data)
