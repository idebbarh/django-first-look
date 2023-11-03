from django.http import  HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

challenges = {
    "january": "Start a daily journal and write at least a paragraph every day.",
    "february": "Learn a new recipe and cook a meal you've never tried before.",
    "march": "Take up a 30-day exercise challenge, such as push-ups, squats, or a daily run.",
    "april": "Begin learning a new language using online resources or apps.",
    "may": "Read a new book or start a reading challenge (e.g., one book a week).",
    "june": "Start a small home improvement project or learn a new DIY skill.",
    "july": "Practice a new hobby, such as drawing, painting, knitting, or playing a musical instrument.",
    "august": "Try a new outdoor activity or sport, like hiking, kayaking, or cycling.",
    "september": "Learn basic coding or take an online course in a subject you're interested in.",
    "october": "Challenge yourself to a digital detox for a weekend or a few days.",
    "november": "Practice gratitude by keeping a daily gratitude journal.",
    "december": "Volunteer or do something to help others in need, especially during the holiday season.",
}

months = list(challenges.keys())


def index(_):
    response_data =  render_to_string("challenges/index.html",{
        "months":months
    })

    return HttpResponse(response_data)


def month_challenge_by_number(_, num):
    if num > 0 and num <= len(months):
        return HttpResponseRedirect(months[num - 1])
    else:
        return HttpResponseRedirect("/NotFound") 


def month_challenge(_, month):
    if month in challenges:
        month_challenge_value = challenges[month]
        response_data = render_to_string("challenges/month-challenge.html",{
            "month_name":month,
            "challenge":month_challenge_value,
        })
        return HttpResponse(response_data)
    else:
        return HttpResponseRedirect("/NotFound") 

