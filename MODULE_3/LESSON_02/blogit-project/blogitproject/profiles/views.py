from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def get_user_profile(request, username):
    if request.method == 'GET':
        profile = get_object_or_404(Profile, user__username=username)
      # profile = Profile.objects.get(user__username=username)
        context = {
            'profile': profile,
        }
        return render(request, 'profiles/profile.html', context=context)
    
@login_required
def edit_user_profile(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    context = {
      'profile': profile,
    }
    if request.method == 'GET':
      if request.user.id == profile.user.id:
        return render(request, 'profiles/edit_profile.html', context=context)
      else:
        return render(request, 'profiles/profile.html', context=context)