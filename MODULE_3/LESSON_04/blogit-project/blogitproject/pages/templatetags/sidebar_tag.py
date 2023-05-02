from django import template
from profiles.models import Profile
from blogs.models import Blog
from comments.models import Comment
from taggit.models import Tag

register = template.Library()


@register.simple_tag
def sidebar_data():
    blogs = Blog.objects.filter(is_published=True)
    recens_blogs = blogs.order_by('-created_at')[:4]
    categories = {category[0]: blogs.filter(category=category[0]).count() for category in Blog.CATEGORY_CHOICE}
    tags = Tag.objects.all()
    unique_tags = set()
    for tag in tags:
        if blogs.filter(tags__name__in=[tag.name] ):
            unique_tags.add(tag)

    data = {
        'recent_blogs' : recens_blogs,
        'categories' : categories,
        'tags' : unique_tags,
    }


    return data 