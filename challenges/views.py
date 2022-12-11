from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": "Say ALLAHU AKBAR"
}


def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })


def monthly_challenge_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Given month is not supported!!")

    redirect_month = months[month-1]
    redirect_path = reverse("monthly-challenge", args=[redirect_month])
    # HttpResponseRedirect("/challenges/"+redirect_month)
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
