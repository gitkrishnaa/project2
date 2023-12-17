from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .forms import UploadFileForm
from django.views.decorators.csrf import csrf_exempt
import os
from . import parser_scrap
# os.makedirs("some/file/") 

@csrf_exempt 
# Create your views here.
def say_hello(request):
  if(request.method=='POST'):
    print(request)
    json_data = {
        'name': 'John Doe',
        'age': 30
    }
    # print(json_data)
    return JsonResponse(json_data)
  if(request.method=='GET'):
    print("hello")
    print(request)
    json_data = {
        'msg': 'plese request by GET method'
    }
    print(json_data)
    return JsonResponse(json_data)
  
i=5
file_locaion="some/file/name"+str(i)+".txt"

def handle_uploaded_file(f):
    global i
    global file_locaion
    i += 1
   
    with open(file_locaion, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    print('handle_uploaded_file')

@csrf_exempt 
def upload_file(request):
    global file_locaion
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print("checking...")
        print(request.FILES)
        print(form.is_valid())
        handle_uploaded_file(request.FILES["file"])
        parser_scrap.extract_text_from_pdf(file_locaion)
        return JsonResponse({'msg':'post method,sucessful, but it is not get file'})     
    else:
     form = UploadFileForm()
     return JsonResponse({'msg':'not sucessful'})