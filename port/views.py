from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    template = 'port/home.html'
    context = {}
    return render(request, template, context)


def new_request(request):
    first_name = request.POST.get('first_name')
    surname = request.POST.get('surname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message1 = request.POST.get('message')
    message = f'{message1} by \n {first_name} {surname} \n my contact number is{phone} \n my email -- {email}'
    subject = 'Message from my portfolio'
    print(first_name)
    print(surname)
    print(email)
    print(phone)
    print(message)
    emailFrom = email
    emailTo = [settings.EMAIL_HOST_USER]
    send_mail(
        subject,
        message,
        emailFrom,
        emailTo,
        fail_silently=True,
    )
    template = 'port/thanks.html'
    return render(request, template)