from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, redirect

from .models import POST


# Create your views here.
def home(request):
    dt = POST.objects.all()
    return render(request,'home.html',{'allpost':dt})

def user_singup(request):
    if request.method == "POST":
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username=username).exists():
            messages.warning(request,f"{username} This username is already taken please enter other username")
            return redirect('singup')
        if len(username) < 3:
            print(len(username))
            messages.warning(request, f"{username} This username is not valid please enter under 3 to 10 letters")
            return redirect('singup')
        if User.objects.filter(email=email).exists():
            messages.warning(request, f"{email} This email id is already existsing.. please enter other email id")
            return redirect('singup')
        if password1  not in password2:
            messages.warning(request, f"{password1} and {password2} This is not same password .. please enter same password")
            return redirect('singup')
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        from django.core.mail import send_mail
        from django.conf import settings
        send_mail(
            'test',
            username,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )

        from twilio.rest import Client
        account_sid = 'AC8992cebfaa3318a3a17075bb38aae8bd'
        auth_token = 'd66915cad6a0f5e5d3a916dcd549e517'
        client = Client(account_sid, auth_token)
        message = client.messages.create(

            body=f"{firstname},{lastname},{email}",
            from_='+18509203659',
            to='+917078711121'
        )
        #

        messages.success(request,f"{username} Your account created successfully")
        return redirect('singin')
    else:
        return render(request,'si.html')
def user_singin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            login(request,user)

            return redirect('showpost')
        else:
            HttpResponseRedirect('/')
    else:
        return render(request,'singin.html')

def user_logout(request):
    logout(request)

    return redirect('home')


def user_post(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user = request.user
            title = request.POST['title']
            post = request.POST['post']
            data = POST(user=user,title=title,post=post)
            data.save()
            dt = POST.objects.filter(user=request.user)
            print(dt)
            # return render(request, 'home.html', {'post':dt})
            return redirect('showpost')
        else:
            # return  render(request,'post.html')
            dt = POST.objects.filter(user=request.user)
            return render(request, 'post.html', {'post': dt})
    else:
        return redirect('singin')


def show_post(request):
    print(request.user)
    user = request.user
    print(user)
    if not request.user.is_authenticated:
        print("if  ",request.user)
        return redirect('singin')
    else:
        dt =POST.objects.filter(user=request.user)
        return render(request, 'showpost.html', {'post': dt})

def user_update(request,id):
    print(id)
    if request.user.is_authenticated:
        if request.method == 'POST':
           utitle = request.POST["utitle"]
           upost = request.POST['upost']
           dt = POST.objects.get(pk=id)
           td = POST(id=id,user=request.user,title=utitle,post=upost,date=dt.date)
           td.save()
           return redirect('showpost')
        else:
            print("heello")
            dt =POST.objects.get(pk=id)
            print(dt)
            return render(request,'test.html',{'data':dt})
    else:
        return redirect('singin')


def user_dalete(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = POST.objects.get(pk=id)
            pi.delete()
        return redirect('showpost')
    else:
        redirect('singin')

def testing(request,id):
    pi = POST.objects.get(pk=id)
    return render(request,'fullpost.html',{'data':pi})

def search(request):
    searching = request.GET['search']
    se1 = POST.objects.filter(title__icontains=searching)
    se2 = POST.objects.filter(post__icontains=searching)
    allpost = se1.union(se2)
    if allpost:
        return render(request, 'search.html', {'se': allpost})
    else:
        return render(request,'search.html',{'no':searching})


