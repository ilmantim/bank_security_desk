from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter_time_format import format_duration


def get_duration(visit):
    return localtime() - localtime(visit.entered_at)


def storage_information_view(request):

    all_visits = Visit.objects.all()

    not_leaved = []

    for visit in all_visits:
        if not visit.leaved_at:
            not_leaved.append(visit)

    non_closed_visits = []

    for visit in not_leaved:
        owner_name = visit.passcard.owner_name
        entered_at = visit.entered_at
        duration = format_duration(get_duration(visit))

    non_closed_visit = {
        'who_entered': owner_name,
        'entered_at': entered_at,
        'duration': duration
    }
    non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
