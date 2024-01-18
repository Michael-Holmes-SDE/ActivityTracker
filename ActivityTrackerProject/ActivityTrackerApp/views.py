from django.shortcuts import render, get_object_or_404, redirect
from .models import Activity, TimeLog
from django.utils import timezone

def index(request):
    activities = Activity.objects.all()
    return render(request, 'core/index.html', {'activities': activities})

def newActivity(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        activity = Activity.objects.create(name=name)
        return redirect('activity', id=activity.id)
    return render(request, 'core/new_activity.html')

def activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    return render(request, 'core/activity.html', {'activity': activity})

def newTimelog(request, id):
    activity = get_object_or_404(Activity, id=id)
    if request.method == 'POST':
        start_time = timezone.datetime.strptime(request.POST.get("start_time"), '%Y-%m-%dT%H:%M')
        end_time = timezone.datetime.strptime(request.POST.get("end_time"), '%Y-%m-%dT%H:%M')
        duration = str(end_time - start_time)

        TimeLog.objects.create(activity=activity, start_time=start_time, end_time=end_time, duration=duration)
        return redirect('activity', id=id)
    return render(request, 'core/new_timelog.html', {'activity': activity})