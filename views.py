from django.http import HttpResponse
import json
from django.shortcuts import render, redirect
from .models import *
import requests
from django.contrib import messages

# Create your views here.

def home(request):
    response=requests.get(f'http://127.0.0.1:8000').json()
    #messages.success(request, 'Data created successfully!')
    #messages.success(request, "Data updated successfully")
    return render(request,"home.html",{'datas':response})

def view(request,id):
    response=requests.get(f'http://127.0.0.1:8000/view/{id}').json()
    return render(request,"view.html",{'datas':response})
def create(request):
    if request.method == 'POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        district=request.POST['district']
        pincode=request.POST['pincode']
        state=request.POST['state']
        gender=request.POST['gender']
        #image=request.FILES['image']

        # Check if required fields are provided

        errors = {}
        if not name:
            errors['name'] = 'Name is required'
        if not mobile:
            errors['mobile'] = 'Mobile no is required'
        if not email:
            errors['email'] = 'Email is required'
        if not district:
            errors['district'] = 'District is required'
        if not pincode:
            errors['pincode'] = 'Pincode is required'
        if not state:
            errors['state'] = 'State is required'
        if not gender:
            errors['gender'] = 'Gender is required'
        #if not image:
            #errors['image'] = 'Image is required'
        
        if errors:
             return render(request, "create.html", {'errors': errors, 'data': request.POST})
        

        data_val={'Name':name,
                    'Mobile':mobile,
                    'Email':email,
                    'District':district,
                    'Pincode':pincode,
                    'State':state,
                    'Gender':gender}
        #files= {'Image':image}
        create_new=requests.post("http://127.0.0.1:8000/create/",data=data_val).json()#files=files
        print(create_new)

        #if 'success' in create_new and create_new['success']:
        messages.success(request, 'Data created successfully!')
        #else:
            #messages.error(request, 'Failed to create data.')
        return render(request,"image.html") 
    else:
        return render(request,"create.html")

def update(request,id):
    if request.method == 'POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        district=request.POST['district']
        pincode=request.POST['pincode']
        state=request.POST['state']
        gender=request.POST['gender']
        #image=request.FILES['image'] 

        errors = {}
        if not name:
            errors['name'] = 'Name is required'
        if not mobile:
            errors['mobile'] = 'Mobile no is required'
        if not email:
            errors['email'] = 'Email is required'
        if not district:
            errors['district'] = 'District is required'
        if not pincode:
            errors['pincode'] = 'Pincode is required'
        if not state:
            errors['state'] = 'State is required'
        if not gender:
            errors['gender'] = 'Gender is required'
        #if not image:
            #errors['image'] = 'Image is required'
        
        if errors:
            update_data = {
                'Name': name,
                'Mobile': mobile,
                'Email': email,
                'District': district,
                'Pincode': pincode,
                'State': state,
                'Gender': gender,
            }
           
            return render(request, "update.html", {'errors': errors, 'datas': update_data})
            


        data_val={'Name':name,
                    'Mobile':mobile,
                    'Email':email,
                    'District':district,
                    'Pincode':pincode,
                    'State':state,
                    'Gender':gender,}
        #files={'Image':image}       
        result=requests.put(f'http://127.0.0.1:8000/update/{id}/',data=data_val)
        #print("result=",result)
        if result.status_code == 200:
            messages.success(request, 'Data updated successfully!')
        else:
            messages.error(request, 'Failed to update data.')
        return redirect('home')
    else:
        update=requests.get(f'http://127.0.0.1:8000/update/{id}').json()
        #print("Update data=",update)   
        return render(request,"update.html",{'datas':update})
    
def image(request,id):
    if request.method == 'POST':
        image=request.FILES['image'] 
        files={'Image':image}
        result=requests.put(f'http://127.0.0.1:8000/update/image/{id}/',files=files)
        print("image change=",files)
        print('----------statuscode-------',result.status_code)
        print('------json------',result.json())
        messages.success(request, 'Profile Updated successfully!')
        return redirect('home')
    else:
        update=requests.get(f'http://127.0.0.1:8000/update/image/{id}').json()
        print("Image=",update)
        return render(request,"image.html",{'datas':update})

def delete(request,id):
    delete_data=requests.delete(f'http://127.0.0.1:8000/delete/{id}')
    return redirect('home')

def head(request):
    response = requests.head(f'http://127.0.0.1:8000/') #http://127.0.0.1:8000/media/image/img3.jpg
    return render(request,"option.html",{'data':response})

def option(request):
    response = requests.options(f'http://127.0.0.1:8000/')
    return render(request,"login.html",{'data':response})






