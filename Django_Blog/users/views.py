from django.shortcuts import render,redirect,get_object_or_404
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm,UpdateProfileForm,UpdateUserForm
from .models import Profile
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

#from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            #messages.success(request,f'Account Created For {username}')
            messages.success(request,f'Account Created Successfuly. Please LogIn to continue...')
            # return redirect('blog-home')
            return redirect('login')
    else :
        #form = UserCreationForm()
        form = UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST,instance=request.user)
        p_form = UpdateProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid :
            u_form.save()
            p_form.save()
            messages.success(request,f'Your Profile has been Updated!')
            return redirect('profile')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request,'users/profile.html',context)




def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'users/user_profile.html', {"user":user})
