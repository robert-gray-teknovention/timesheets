from django.shortcuts import render
from django.http import JsonResponse
from .serializers import EmailSerializer
from django.core.mail import EmailMessage
import re
import json


def email(request):
    if request.method == 'POST':
        data = json.loads(request.POST.get('email'))
        serializer = EmailSerializer(data=data)
        if serializer.is_valid():
            # Send email
            recipients = re.split(r'[,;]', data['recipients'][0].replace(' ', ''))
            for r in recipients:
                email = EmailMessage(data['subject'], data['message'], to=[r],
                                     reply_to=['mailer@mail.teknovention.com'])
                # email = EmailMessage(data['subject'], data['message'], to=recipients)
                email.send()
            serializer.save()
            return JsonResponse({"message": "Email sent and saved"})
        else:
            return JsonResponse(status=404, data={'status': 'false', 'message': 'Email failed'})
    return render(request, 'tsmanagement/managedashboard.html')