import django
from django.shortcuts import render
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Bookentry
from .models import Product

# Create your views here.
# This function for home 
def home(request):
    return HttpResponseRedirect('/books/')

def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            # nm = fm.cleaned_data['username']
            # fn = fm.cleaned_data['first_name']
            # ln = fm.cleaned_data['last_name']
            # em = fm.cleaned_data['email']
            # pm = fm.cleaned_data['password1']
            # pm2 = fm.cleaned_data['password2']
            # reg = User(username=nm, first_name=fn, last_name=ln, email=em,password1=pm,password2=pm2)
            # reg.save()
            fm.save()
            messages.success(request, 'Account created successfully')
    else:                                                    # This is for get request
        fm = SignUpForm()
    return render(request, 'hello1/signup.html', {'form': fm})
    

# This function is for login user/superuser
def log_in(request):
 if not request.user.is_authenticated:            # user not already login
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            ename = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']

            user = authenticate(email=ename, password=upass)
            if user is not None:
                login(request, user)
                if request.user.is_staff == True:        # this condition is for staff/admin user 
                    return HttpResponseRedirect('/addshow/')  # only staff user can redirect this path
                else:
                    return HttpResponseRedirect('/books/')  # for loacal user (no staff permission)
                         
    else:                                    # This is get request
        fm = LoginForm()          
    return render(request, 'hello1/login.html', {"form": fm})  # login form will show
 else:
     if request.user.is_staff==True:
        return HttpResponseRedirect('/addshow/')  # if satff/admin has already login then this condition will active
     else:
         return HttpResponseRedirect ('/books/')   # for already login local user
 
 

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')  # user will go to the login page after logout


#this function is for adding new book an show item 

def add_show(request):
    if request.user.is_staff == True:    # only staff/admin user can add/show books 
    
        if request.method == 'POST':        # if request is post then this condition will active
            fm = Bookentry(request.POST,request.FILES)     
            if fm.is_valid():
                nm=fm.cleaned_data['name']
                an=fm.cleaned_data['auth_name']
                pr=fm.cleaned_data['price']
                im=fm.cleaned_data['image']
                ds=fm.cleaned_data['description']
                reg=Product(name=nm,auth_name=an,price=pr,description=ds,image=im)
                reg.save()
                fm=Bookentry()         
            # we can use this method also fm.save()
        else:    
            fm = Bookentry()               # This is get request books entry form will show
        stud = Product.objects.all()      # All objects are retrive by this query set
        return render(request,'hello1/addshow.html',{'form':fm,'stu':stud})  
    else:
        return HttpResponseRedirect('/books/')    # this is for local user 


# This function delete objects and only staff/admin can do this 
def delete(request,id):
    if request.user.is_staff == True:
        if request.user.is_authenticated:
          if request.method == 'POST':
            
             pi=Product.objects.get(pk=id)
             pi.delete()
             return HttpResponseRedirect('/addshow')
        else:
            return HttpResponseRedirect('/login/')      
         
    else:
        return HttpResponseRedirect('/books')     

#update book
# def updatebook(request,id):
#         pi=Product.objects.get(pk=id)
#         # fm=StudentRegistartion(instance=pi) 
#         return render(request,'store/updatebook.html',{'pi':pi})

# This function will update the objects information and only staff/admin can do this
def updatebook(request,id):
    if request.user.is_staff == True:
        if request.method =="POST":
            pi=Product.objects.get(pk=id)
            fm=Bookentry(request.POST,request.FILES,instance=pi)
            if fm.is_valid():
                fm.save()
        else:
            pi=Product.objects.get(pk=id)
        fm=Bookentry(instance=pi) 
        return render(request,'hello1/updatebook.html',{'form':fm})
    else:
        return HttpResponse('soory you are not Authorize') 
    
# This function is for our user and it will only show books

def user_books(request):
    # if request.user.is_authenticated:
    books=Product.objects.all()
    return render(request,'hello1/books.html',{'books':books})