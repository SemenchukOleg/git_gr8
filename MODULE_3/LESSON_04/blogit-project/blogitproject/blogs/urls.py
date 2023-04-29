from django.urls import path

from blogs import views

urlpatterns = [
    path('<slug:author>/<slug:slug>/view', views.single_blog, name='single_blog'),
    path('blog/create', views.create_blog, name='create_blog'),
    path('blog/<slug:author>/<slug:slug>/edit', views.edit_blog, name='edit_blog'),
    path ('blog/<slug:author>/<slug:slug>/delete', views.delete_blog, name='delete_blog'),
    path ('blog/<slug:author>/<slug:slug>/add-comment-to-blog', views.add_comment_to_blog, name='add_comment_to_blog'),
    path ('blog/add-or-remove-like-ajax', views.add_or_remove_like_ajax, name='add_or_remove_like_ajax'),

]
