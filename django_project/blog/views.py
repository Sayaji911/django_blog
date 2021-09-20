from django.shortcuts import render

posts = [{
    'author': 'CoreyMS',
    'title': 'Blog Post 1',
    'content': 'This is is just to check jinja',
    'date_posted': 'September 20 2021'

},
    {
    'author': 'Sayaji',
    'title': 'Blog Post 2',
    'content': 'This is is just to check jinja again',
    'date_posted': 'September 20 2021'
}

]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})
