from django import template
from profiles.models import Profile
from blogs.models import Blog
from comments.models import Comment


register = template.Library()


@register.simple_tag
def profile_activity_counter(username):
    profile = Profile.objects.get(user__username=username)
    blogs = Blog.objects.filter(is_published=True)
    comments = Comment.objects.filter(author=profile)
    data_counter = {
        'blogs_data': blogs.filter(author=profile).count(),
        'comments_data': comments.count(),
        'likes_data' : blogs.filter(likes__contains=[profile.id]).count(),
        
    }

    return data_counter