from django.shortcuts import render

from django.http import JsonResponse
from datetime import datetime, timedelta
import os


# Create your views here.


def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    github_url = f"https://github.com/jsmtcode/HNGx_projects"
    github_source_url = "https://github.com/jsmtcode/HNGx_projects/blob/master/app/views.pyclear"

    # Calculate the current day of the week
    current_day = datetime.now().strftime('%A')

    # Calculate the current UTC time with validation of +/-2 hours
    current_utc_time = datetime.utcnow()
    current_utc_time += timedelta(hours=1) 

    response_data = {
        'slack_name': slack_name,
        'current_day': current_day,
        'utc_time': current_utc_time.strftime("%Y-%m-%dT%H:%M:%SZ"),
        'track': track,
        'github_file_url': github_source_url,
        'github_repo_url': github_url,
        'status_code': 200
    }

    return JsonResponse(response_data)
