from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm, UserProfileForm, EditProfileForm, EditUserForm
from .models import UserProfile
from django.contrib.auth.forms import PasswordChangeForm
def login_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "form.html", {"form":form, "title": title})


def register_view(request):
    print(request.user.is_authenticated())
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    profileForm = UserProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid() and profileForm.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        profile = profileForm.save(commit=False)
        profile.user = user
        profile.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")

    context = {
        "form": form,
        "title": title,
        "profileForm": profileForm,
    }
    return render(request, "form.html", context)


def logout_view(request):
    logout(request)
    return redirect("/")


def edit_profile(request):
    if request.method == 'POST':
        userform = EditUserForm(request.POST, request.FILES or None, instance=request.user)
        profileform = EditProfileForm(request.POST, request.FILES or None, instance=request.user)
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            profile = profileform.save(commit=False)
            profile.user = user
            profile.save()

            print("Form Updated")
            return redirect('profile')
        else:
            print('Error Occurred While Updating.')
            return redirect('posts:list')
    else:
        form = EditUserForm(instance=request.user)
        profileForm = EditProfileForm(instance=request.user)
        context = {'form': form, 'profileForm': profileForm}
        return render(request, 'EditProfile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('logout')
        else:
            print('Error Occurred While Updating.')
            return redirect('posts:list')
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form}
        return render(request, 'EditPassword.html', context)
