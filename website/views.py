from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordFrom 
from .models import Record

def home(request):
   records=Record.objects.all()
   #check to see if user is logged in
   if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']
       #Authenticate user
       user=authenticate(request,username=username,password=password)
       if user is not None:
           login(request,user)
           messages.success(request,"You have been logged in")
           return redirect('home')
       else:
           messages.success(request,"Error logging in, Please try again")
           return redirect('home')
   else: 
       return render(request,'home.html',{'records':records})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')


def register_user(request):
    #fetch data from database
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Athenicate user
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1') 
            user=authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered")
            return redirect('home')
        
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})    
       
    return render(request,'register.html',{'form':form})    


        

def customer_record(request,pk):
    if  request.user.is_authenticated:
        customer_record=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer_record':customer_record})

    else:
        messages.success(request,"Please login to view customer record")
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
     delete_record=Record.objects.get(id=pk)
     delete_record.delete()
     messages.success(request,"Record deleted successfully")
     return redirect('home')
    
    else:
        messages.success(request,"Please login to delete customer record")
        return redirect('home')



def add_record(request):
    form=AddRecordFrom(request.POST or None)
    if request.user.is_authenticated:
        if request.method=="POST":
            if form.is_valid():
                add_record=form.save(commit=False)
                messages.success(request,"Record added successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,"Please login to add customer record")
        return redirect('home')
