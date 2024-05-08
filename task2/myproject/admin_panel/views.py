from django.shortcuts import render, redirect  #added redirect
#added by me:
from .models import App
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

#added by me
def admin(request):
    if request.method =='POST':
        
        # app_icon = request.POST.get('app_icon')
        app_icon = request.FILES.get('app_icon')
        
        app_name = request.POST.get('app_name')
        app_link = request.POST.get('app_link')
        app_category = request.POST.get('app_category')
        sub_category = request.POST.get('sub_category')
        points = request.POST.get('points')

        fb = App(app_icon=app_icon, app_name=app_name,app_link=app_link,app_category=app_category,sub_category=sub_category,points=points)
        fb.save()
        
        return render(request, 'admin.html')


    a = App.objects.all()
    # aa = App.objects.filter(app_name='Facebook').values()

    # print(aa)
    return render(request, 'admin.html')

def signin(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'registration successful')
                return redirect('register')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

        
        

    else:
        return render(request, 'register.html')
    

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'login successful')
            return render(request, 'admin.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')