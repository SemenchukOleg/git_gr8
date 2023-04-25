from django.shortcuts import render, redirect
from profiles.models import Profile
from blogs.models import Blog
from django.contrib.auth.decorators import login_required


# Create your views here.
def single_blog(request, author, slug):
    profile = Profile.objects.get(user__username=author)
    blog = Blog.objects.get(author=profile, slug=slug)

    context = {
        'blog' : blog,
        'profile' : profile,
    }

    return render(request, 'blogs/single_blog.html', context=context)

@login_required
def create_blog(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    categories = [category[0] for category in Blog.CATEGORY_CHOICE]
    context = {
        'profile': profile,
        'categories': categories,
    }

    if request.method == 'GET':
        return render(request, 'blogs/create_blog.html', context=context)

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        category = request.POST['category']

        #create blog
        blog = Blog()
        blog.title = title
        blog.text = text
        blog.category = category
        blog.author = profile
        try:
            if any(request.FILES):
                blog.image = request.FILES['image']
        except:
            return render(request, 'blog/create_blog.html', context=context)
        blog.save()

        return redirect('/profiles/{}'.format(user.username))