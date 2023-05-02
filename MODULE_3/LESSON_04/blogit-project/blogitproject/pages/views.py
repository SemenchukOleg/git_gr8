from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blogs.models import Blog
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    blogs = Blog.objects.filter(is_published=True)

    query_string = ''

    # search
    search = request.GET.get('search', '')
    if search:
        blogs = blogs.filter(text__icontains=search)
        query_string += f'&search={search}'

    #sort_by
    sort_by = request.GET.get('sort_by', '')
    if sort_by:
        sort_by_dict= {
            'a-z': 'title',
            'z-a': '-title',
            'new-old': '-created_at',
            'old-new': 'created_at',
        }
        blogs = blogs.order_by(sort_by_dict[sort_by])
        query_string += f'&sort_by={sort_by}'

    #category
    category = request.GET.get('category', '')
    if category:
        blogs = blogs.filter(category=category)
        query_string += f'&category={category}'

    #filter by tag
    filter_by_tag = request.GET.get('filter_by_tag', '')
    if filter_by_tag:
        blogs = blogs.filter(tags__name=filter_by_tag)
        query_string += f'&filter_by_tag={filter_by_tag}'

    #Paginator
    paginator = Paginator(blogs, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'blogs': page_obj, #blogs
        'query_string' : query_string,
    }
    return render(request, 'pages/index.html', context=context)  