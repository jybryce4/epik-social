from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from blog.models import Post


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You may now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})

@login_required # settings profile; public profile in blog app
def profile(request):
    user = request.user
    user_posts = Post.objects.filter(author=user).order_by('-date_posted')[:5]
    if request.method == 'POST': # runs when form is submitted
        u_form = UserUpdateForm(request.POST, instance=request.user) # populates forms 
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile) # populates forms; user image upload handling

        if u_form.is_valid() and p_form.is_valid(): # save info only if valid
            u_form.save()
            p_form.save()
            messages.success(request, "Account Updated!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user) # populates forms 
        p_form = ProfileUpdateForm(instance=request.user.profile) # populates forms

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user_posts': user_posts,
        'user': user
    }

    return render(request, 'users/profile.html', context)





