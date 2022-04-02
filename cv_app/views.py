from django.shortcuts import render, redirect
from .models import Email
from .forms import EmailForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

def home(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            const_email = form.save(commit=False)
            send_mail(
                const_email.subject,
                "Name: " + const_email.name + '\n' + "Email: " + const_email.email + "\n" + "Message: " + const_email.message + ".",
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                fail_silently = False,
            )
            print("Email sended")
            form = EmailForm()
            return redirect('home')
    else:
        form = EmailForm()
    context = {'form':form}
    return render(request, 'cv_app/home.html', context)


    
