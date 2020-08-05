from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request,'den/index.html',{})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        # send and Email
        send_mail(
        message_name, # subject
        message, # message
        message_email, # from email
        ['your email'], #to email
        )

        return render(request,'den/contact.html',{'message_name':message_name})
    else:
        return render(request,'den/contact.html',{})

def pricing(request):
    return render(request,'den/pricing.html',{})

def service(request):
    return render(request,'den/service.html',{})

def appointment(request):
    if request.method == "POST":
        yname = request.POST['name']
        yphone = request.POST['phone']
        yemail = request.POST['email']
        yaddress = request.POST['address']
        yscheldule = request.POST['scheldule']
        ytime = request.POST['time']
        ymessage = request.POST['message']


        # myappointment = 'Name: " + yname + " " + "Phone: " + yphone + " " + "Email: " + yemail + " " + "Address: " + yaddress " " + "Scheldule: " + scheldule + " " + "Date: " + ytime + " " + "Message: " + ymessage'
        myappointment =  yname + yphone + yemail + yaddress + yscheldule + ytime + ymessage
        # send and Email

        send_mail(
        'Appointment Request',
        myappointment, # subject
        yemail, # from email
        ['your email'], #to email
        )

        return render(request,'den/appointment.html',{
                'yname':yname,
                'yphone':yphone,
                'yemail':yemail,
                'yaddress':yaddress,
                'yscheldule':yscheldule,
                'ytime':ytime,
                'ymessage':ymessage
                            })
    else:
        return render(request,'den/index.html',{})
