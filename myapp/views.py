from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    return render(request, 'form.html')

# def process(request):
#     a =int(request.POST["num1"])
#     b =int(request.POST["num2"])
#     c =int(request.POST["num3"])
#     d =int(request.POST["num4"])
#     e =int(request.POST["num5"])
#     ans = a + b + c + d + e
#     per = ans / 5

#     if per >= 80:
#         per = str(per) + " Grade First "
#     elif per >= 70 and per < 80:
#         per = str(per) + " Grade Second "
#     else:
#         per = str(per) + " Fail "
#     return render(request, 'result.html', {'Sum': ans, 'Percentage': per})

def process(request):
    
    a = request.POST["txt1"]

    myfile = request.FILES['file123']
    fs = FileSystemStorage()
    myfileupload = fs.save(myfile.name, myfile)
    uploaded_file_url =fs.url(myfileupload)
    print("URL: " + uploaded_file_url)
    return redirect(form)
    # return render(request, 'result.html', {'Name': a})

