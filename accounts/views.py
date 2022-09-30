from django.contrib.auth import authenticate, login ,get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import ContactForm, LoginForm , RegisterForm 


# Create your views here.
def home_page(requedt):
    return HttpResponse("HELLO WORLD THE AUCTION WILL BE THE BEST!")

def accounts(request):
    contact_form = ContactForm(request.POST or None)
    context={
        "title":"Acounts",
        "content":"Welcome to the Account Profile ",
        "form":contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    #if request.method == "POST":
    #    #print(request.POST)
    #    print(request.POST.get('fullname'))
    #    print(request.POST.get('email'))
    #    print(request.POST.get('content'))
    return render(request, 'accounts/accounts.html', context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context  ={
        "form":form
    }
    print("User Logged In")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            #Redirect to success page.
            #context["form"] = LoginForm()
            return redirect('/')
        else:
            # Return am invalid login error and message
            print("error")
    return render(request,'auth/login.html',context)


User = get_user_model()   
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email    = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request,'auth/register.html',context)    

def account(request,pk): 
    context={
        "title":"User Accounts",
        "content":"This is your person account profile"
    }
    return render(request, 'accounts/single-accounts.html',context)