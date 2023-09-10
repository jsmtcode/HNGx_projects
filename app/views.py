from django.shortcuts import render

from django.http import JsonResponse
from datetime import datetime, timedelta
import os


# Create your views here.


def get_info(request):
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')
    github_url = f"https://github.com/jsmtcode/HNGx_projects"
    github_source_url = "https://github.com/your/repo/source_code.py"

    # Calculate the current day of the week
    current_day = datetime.now().strftime('%A')

    # Calculate the current UTC time with validation of +/-2 hours
    current_utc_time = datetime.utcnow()
    current_utc_time -= timedelta(hours=2) 

    response_data = {
        'slack_name': "iheanyi_okeh",
        'current_day_of_week': current_day,
        'current_utc_time': current_utc_time.isoformat(),
        'track': "Backend",
        'github_url_of_file_being_run': github_url,
        'github_url_of_file_source_code': github_source_url,
        'status_code': 200
    }

    return JsonResponse(response_data)
