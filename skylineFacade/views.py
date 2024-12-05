from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from skylineFacade.models import *
from django.views.decorators.csrf import csrf_protect


def home(request):
    services = Services.objects.all()
    blogs = BlogPost.objects.all()
    projects = MajorProjects.objects.all()[:6]
    return render(request,'index.html',{'services':services,'blogs':blogs,'projects':projects})


def aboutus(request):
    return render(request,'aboutus.html')

def projects(request):
    projects = MajorProjects.objects.all()
    return render(request,'projects.html',{'projects':projects})

def projectsDetails(request,slug):
    project = get_object_or_404(MajorProjects, slug=slug)
    return render(request,'project_details.html',{'project':project})

def careers(request):
    return render(request,'careers.html')

def services(request):
    services = Services.objects.all()
    return render(request,'services.html',{'services':services})


def services_details(request,slug):
    service = get_object_or_404(Services, slug=slug)
    return render(request,'services_details.html',{'service':service})


def contact_us(request):
    return render(request,'contactus.html')

def blogs(request):
    blogs = BlogPost.objects.all()
    return render(request,'blogs.html',{'blogs':blogs})


def blogs_details(request,slug):
    blogs = get_object_or_404(BlogPost, slug=slug)
    return render(request,'blog_details.html',{'blogs':blogs})


def Facade_Engineering_Services(request):
    return render(request,'facade-engineering-services.html')


def Facade_Design_Consultancy(request):
    return render(request,'facade-eng-consultancy.html')


def products(request):
    products = Products.objects.get(slug = '1-products')
    
    return render(request,'product.html',context={'product':products})


def upvcWindows(request):
    return render(request,"upvcWindows.html")


def Aluminum_Doors_Windows(request):
    return render(request,"Aluminum_Doors_Windows.html")

def facade_system(request):
    return render(request,"facade_system.html")

def point_fixed(request):
    return render(request,"point_fixed.html")

def louvers(request):
    return render(request,"louvers.html")

def balustrade(request):
    return render(request,"balustrade.html")

def glass_partition(request):
    return render(request,"glass_partition.html")

def street_structure(request):
    return render(request,"street_structure.html")



# def mail_sender():
#     subject = "Indoor OTP Verification"
#     body = f"Good Day, Here is you OTP to signup {generateOTP(6)}"
#     print("body",body)
#     # Create email message
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = receiver_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     try:
#         # Connect to the Gmail SMTP server
#         with smtplib.SMTP("smtp.gmail.com", 587) as server:
#             server.starttls()  # Upgrade the connection to secure
#             server.login(sender_email, sender_password)  # Log in to the server
#             server.send_message(message)  # Send the email

#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email: {e}")