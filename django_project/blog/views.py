from django.shortcuts import render

posts = [
    {
        'author': 'Ali',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 15, 2021'
    },
    {
        'author': 'Buse',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 15, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
