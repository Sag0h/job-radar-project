from django.shortcuts import render

from jobs.models import Job


def job_list(request):
    jobs = Job.objects.filter(
        is_active=True
    ).order_by("-first_seen_at")

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs,
        },
    )