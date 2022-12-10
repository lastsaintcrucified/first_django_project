from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "say SUBAHANALLAH",
    "february": "say ALHAMDULILLAH",
    "march": "say ALLAHUAKBAR",
    "april": "say LA ILAHA ILLALLAH",
    "may": "Make some dua",
    "june": "MAke some prayer",
    "july": "say  LA HAOLA WALA QUWATA ILLA BILLAH",
    "august": "say SUBAHANALLAH 8 times",
    "september": "say SUBAHANALLAH 9 times",
    "october": "say SUBAHANALLAH 10 times",
    "november": "say SUBAHANALLAH 11 times",
    "december": "say SUBAHANALLAH 12 times"
}


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Given month is not supported!!")

    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Given month is not supported!!")
