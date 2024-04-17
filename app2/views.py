
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from requests import Response
from .models import *


from rest_framework import generics, mixins, viewsets
from .serlizer  import *

from .form import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .form import Form_login
from django.contrib.auth import login,authenticate
@login_required(login_url='login')
def home(request):
    doctor=Profile.objects.all()
    context={
        'mydoctor':doctor
    }
    return render (request,'home.html',context=context)

@login_required(login_url='login')
def detal_doctor(request,slug):

     detal_doctor=Profile.objects.get(slug=slug)
     context={
        'detal_doctor':detal_doctor
    }
     return render (request,'detal_doctor.html',context=context)
def Login_user(request):
    form = Form_login()

    if request.method == 'POST':
        form = Form_login(request.POST)
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                return redirect('/')  # Replace 'home' with the name of the view you want to redirect to after successful login
        else:
                form=Form_login()  # Reset the form if authentication fails

    return render(request, 'login.html', {'form': form})
@login_required(login_url='login')
def myprofile(request):
   doctor=Profile.objects.all()
   context={
        'doctor':doctor
   }

   return render(request,'myprofile.html',context=context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')
def form(request):

    user_form=Update_form(instance=request.user)
  
   
        
    if request.method=='POST':
      user_form=Update_form(request.POST,instance=request.user)
  
      if user_form.is_valid():
            user_form.save()
           
            return redirect('vizeta')
     

    
    return render(request,'form.html',context={
        'user_form':user_form,
       
    })



def signup(request):
    if request.method=='POST':
        signup=UserCreationForms(request.POST)
        
        if signup.is_valid():
            signup.save()
            return redirect('login')
    else:
            signup=UserCreationForms()



    return render(request,'signup.html',
                  context={'signup':signup}
                  )





class Mixin(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Mixin_user(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delet(self,request,pk):
        return self.destroy(request)
class Mixin_blog(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Blogs.objects.all()
    serializer_class=Blog_ser
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class Mixin_doctor(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=ExpertDoctor.objects.all()
    serializer_class=Expert_ser
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)



















# =========================={medical}
@login_required(login_url='login')
    
def index(request):
    
        
    
    
        
    if request.method=='POST':
        
     
      x=request.POST.get('name')
      y=request.POST.get('number')
      z=request.POST.get('doctor')
      e=request.POST.get('age')
      f=request.POST.get('gender')
      h=request.POST.get('data')
      
     
      s=LOGIN(name1=x,number=y,doctor=z,age=e,gender=f,data=h)
     
      s.save()
     
    last={
     "item":LOGIN.objects.all()
    }
    
    return render(request,'index.html',context=last)
@login_required(login_url='login')      
def nav(request):
    return render(request,'navbar.html')
@login_required(login_url='login')
def home2(request):
    return render(request,'home2.html')   

@login_required(login_url='login')
def serves(request):
    

    return render(request,'servec.html')
@login_required(login_url='login')
@login_required(login_url='login')
def blog(request):

    return   render(request,'blog.html')
@login_required(login_url='login')
def about(request):

    return render(request,'about.html')

@login_required(login_url='login')
def foter(request):

    return render(request,'conect.html')




@login_required(login_url='login')
    
def Comment(request):
    
        
    
    
        
    if request.method=='POST':
        
     
      N=request.POST.get('name')
      e=request.POST.get('email')
      co=request.POST.get('comment')
      image=request.POST.get('image')
      
     
      
     
      sav=Comments(Name=N,email=e,comment=co,img=image)
      if sav is not None:
            
     
        sav.save()
   
     
    comment={
     "comments":Comments.objects.all()
    }
    
    return render(request,'comment.html',context=comment)



# ======================================================={Dashbord}

@login_required(login_url='login')
def Dash(request):
    show_pation=LOGIN.objects.all()
    context={
    "show_pation":show_pation
    }

    return render(request,'dashbord.html',context=context)

from django.shortcuts import render, redirect

@login_required(login_url='login')
def delete_p(request,pk):
    dlete=LOGIN.objects.get(id=pk)
    if request.method=='POST':
        dlete.delete()


        
    contect={
        'delete':dlete
    }
    return render(request,'delete_p.html',context=contect)
@login_required(login_url='login')
def update(request,pk):
    blogs=LOGIN.objects.get(id=pk)
    form=Loginform(instance=blogs)
    if request.method=='POST':
        form=Loginform(request.POST,instance=blogs)
        if form.is_valid():
            form.save()
         
    context={
        'form':form
    }
    return render (request,'update_p.html',context=context)
from django.contrib import messages


@login_required(login_url='login')
def Dash_doctor(request):
    show_doctor=Profile.objects.all()
    context={
    "show_doctor":show_doctor
    }

    return render(request,'dasbord_doctor.html',context=context)

def update2(request,pk):
    profile=Profile.objects.get(id=pk)
    form=Update_profile(instance=profile)
    if request.method=='POST':
        form=Update_form(request.POST,instance=profile)
        if form.is_valid():
            form.save()
         
    context={
        'form':form
    }
    return render (request,'update_p2.html',context=context)
def delete_d(request,pk):
    dlete=Profile.objects.get(id=pk)
    if request.method=='POST':
        dlete.delete()


        
    contect={
        'delete':dlete
    }
    return render(request,'delete_d.html',context=contect)


@login_required(login_url='login')
def callUs(request):

    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')

        detal=Callus(firstname=fname,lastname=lname,youremail=email,numberphone=phone,masseg=message)
        detal.save()

    return render(request,'callus.html')




@login_required(login_url='login')
def blog(request):
    blog=Blogform()
    context={
        'blog':blog,
        'item':Blogs.objects.all()
    }
  

    return render (request,'blog.html',context=context)



def AddBlog(request):


    if request.method=='POST':
        
        names=request.POST.get('name')
        titles=request.POST.get('title')
        discribtions=request.POST.get('desc')
        dat=request.POST.get('date')
        image=request.POST.get('img')
        detal=Blogs(name=names,title=titles,discribtion=discribtions,date=dat,img=image)
        detal.save()



    return render(request,'add_blog.html')




def updateComment(request,pk):
    coment=Comments.objects.get(id=pk)
    form=Comments_Form(instance=coment)
    if request.method=='POST':
        form=Comments_Form(request.POST,instance=coment)
        if form.is_valid():
            form.save()
         
    context={
        'form':form
    }
    return render (request,'update_comment.html',context=context)

def deleteComment(request,pk):
    dlete=Comments.objects.get(id=pk)
    if request.method=='POST':
        dlete.delete()


        
    contect={
        'delete':dlete
    }
    return render(request,'deleteComment.html',context=contect)

@login_required(login_url='login')
def Expertdoctors(request):
    doctor=ExpertDoctor.objects.all()
    context={
        'mydoctor':doctor
    }
    return render (request,'doctor.html',context=context)
