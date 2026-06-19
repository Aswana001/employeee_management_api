from django.shortcuts import render

from datetime import datetime

from django.utils.timezone import make_aware

from .tasks import send_email_task


def home(request):

    success = False

    if request.method == "POST":

        subject = request.POST.get('subject')

        message = request.POST.get('message')

        from_email = request.POST.get('from_email')

        to_email = request.POST.get('to_email')

        schedule_time = request.POST.get('schedule_time')

        schedule_time = datetime.fromisoformat(
            schedule_time
        )

        schedule_time = make_aware(
            schedule_time
        )

        send_email_task.delay(

          subject,
          message,
          from_email,
          to_email
     )
        success = True

    return render(request, 'index.html', {
        'success': success
    })