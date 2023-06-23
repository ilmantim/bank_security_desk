from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime, now
from datetime import timedelta
from datacenter_time_format import format_duration


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        current_time = now()
        duration = current_time - visit.entered_at
    else:
        duration = visit.leaved_at - visit.entered_at

    limit_time = timedelta(minutes=minutes)
    return duration > limit_time


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        entered_at = localtime(visit.entered_at)
        if visit.leaved_at:
            leaved_at = localtime(visit.leaved_at)
            duration = leaved_at - entered_at
        else:
            current_time = now()
            duration = current_time - entered_at

        duration_str = format_duration(duration)
        is_strange = is_visit_long(visit, minutes=60)

        visit_info = {
            'entered_at': entered_at,
            'duration': duration_str,
            'is_strange': is_strange
        }
        this_passcard_visits.append(visit_info)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)

