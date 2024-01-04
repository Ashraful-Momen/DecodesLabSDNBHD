from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

def home(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/home.html',)

def about(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/about.html',)

def technology(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/technology.html',)


def contact(request):
    if request.method == 'POST':
        # print(request.POST)  # Check if form data is being received
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully.')
#             return redirect('contact')  # Redirect to the same contact page to show only the success message
        else:
            messages.error(request, 'All fields are required.')

        # print(messages.get_messages(request))  # Check if messages are being set

    return render(request, 'Pages/contact.html')


#service ------------------------------------------------------------

def cloud(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/cloud.html',)

def bigData(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/bigData.html',)

def dataAnalysis(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/dataAnalysis.html',)

def devOps(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/devOps.html',)

def iot(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/iot.html',)

def ml(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/ml.html',)

def ai(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/ai.html',)

def dataSecurity(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/dataSecurity.html',)

def cyber(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/cyber.html',)

def uiux(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/ux.html',)

def software(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/software.html',)

def application(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/Application.html',)

def crm(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/crm.html',)

def eLearning(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/eLearning.html',)

def ecommerce(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/ecommerce.html',)

def erp(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/erp.html',)

def SmartFarming(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/SmartFarming.html',)

def hospital(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/hospital.html',)

def assetManagement(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/assetManagement.html',)

def pos(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/pos.html',)
def chain(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/chain.html',)
def human(request):
    # Retrieve all items and pass them to the template
    # items = Item.objects.all()  # Replace with your method of fetching items
    return render(request, 'Pages/human.html',)
