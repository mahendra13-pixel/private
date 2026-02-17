from django.shortcuts import render ,redirect
from .models import *
from django.contrib import messages
from   django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError 
from   django.contrib.auth import authenticate ,login ,logout
import re
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def index(request):
    title =Category.objects.all()   
    momo= Momo.objects.all()
    cateid = request.GET.get("category")
    if cateid =='all':
      momo= Momo.objects.all()
    elif cateid :
        momo =Momo.objects.filter(category=cateid)
    else :
         momo= Momo.objects.all()
    if request.method =='POST':
        data=request.POST
        name=data['name']
        phone=data['phone']
        email=data['email']
        message=data['message']
        user =Detail(name=name,phone=phone,email=email,message=message)
        user.save()
        messages.success(request,f'hey {name} your form submit')
        return redirect('index')
    context = {
        'messages':messages,
        'item':momo,
        'title':title
        }
    
    return render(request,'core/index.html',context)

@login_required(login_url='log_in')
def menu(request):
    category = Category.objects.all()
    return render(request,'core/menu.html',{"category":category})

def about(request):
    return render(request,'core/about.html')
def services(request):
    return render(request,'core/services.html')
def contact(request):
    return render(request,'core/contact.html')

def testemonial(request):
    data= Detail.objects.all()
    return render(request,'core/testemonial.html',{'data':data})
def terms(request):
    return render(request,'core/terms.html')
def privacy(request):
    return render(request,'core/privacy.html')


#--------------------Aut-part--------------------
def register(request):
    if request.method == 'POST':
        fname =request.POST['fname']
        lname =request.POST['lname']
        mail =request.POST['mail']
        username =request.POST['username']
        password =request.POST['password']
        password1 =request.POST['password1']
        if password == password1:
            error=[]
            if User.objects.filter(username=username).exists():
                 error.append('username is already exists')
            if User.objects.filter(email=mail).exists():
                 error.append('email is already exists')
            if not re.search(r'[A-Z]',password):
                error.append('at least on upper case need')
            if not re.search(r'\d',password):
                error.append('at least one digit need')
            if not re.search(r'\W',password):
                error.append('at least on special charecter needed')
            
            try:
                validate_password(password)
                if not error:
                    User.objects.create_user(first_name=fname,last_name=lname,username=username,password=password,email=mail,)
                    messages.success(request,"login sucessfully")
                    return redirect('register')
                else:
                    for i in error:
                        messages.error(request,i)
                    return redirect("register")
            except ValidationError as e:
                for error in e.messages:
                    messages.error(request,error)
                return redirect('register')


        else:
            return redirect('register')
    return render(request,'accounts/register.html')
def log_in(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember_me =request.POST.get('remember_me')
        if not User.objects.filter(username=username).exists():
            messages.error(request,"username doesnot valid")
            return redirect('log_in')
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            if remember_me:
                request.session.set_expiry(1800)
            else:
                request.session.set_expiry(0)
            
            next = request.POST.get('next')
            return redirect(next if next else "index")
    next = request.GET.get('next','')
    return render(request,'accounts/login.html',{"next":next})
def log_out(request):
    logout (request)
    return redirect('log_in')
@login_required(login_url='log_in')
def pass_change(request):
    form =PasswordChangeForm(user=request.user)
    if request.method =='POST':
        form =PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_in')
    return render(request,'accounts/pass_change.html',{'form':form})
