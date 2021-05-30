from django.shortcuts import render

posts = [
    {
        'title': 'Blog Post 1',
        'author': 'Turab45',
        'content': 'This is the first post',
        'date_posted': 'May 30, 2020'
    },
    {
        'title': 'Blog Post 2',
        'author': 'Turab Bajeer',
        'content': 'This is the Second post',
        'date_posted': 'June 1, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
