from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
import random

def index(request):
    return render(request,'index.html')
def sendmail(request):
    global message
    email=request.POST['email']
    subject = 'donotreply'
    n=random.randint(111111,999999)
    n=str(n)
    message =n
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'login.html')
def login(request):
    if request.method=="POST":
        otp=request.POST['otp']
        print(otp)
        print(message)
        if message==otp:
            return render(request,'sent.html')
    return render(request,'login.html')    
