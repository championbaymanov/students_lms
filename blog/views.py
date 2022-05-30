from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from requests import post
from blog.models import Post, Category, Comment
from videos.models import VideoContent
from hitcount.views import HitCountDetailView
from blog.forms import CommentForm, PostCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.

def searchBlog(request):
    context = {}
    posts = Post.objects.all().filter().order_by('-id')

    if request.method == "GET":
        query = request.GET.get("search")
        queryset = posts.filter(Q(title__icontains=query))

        page = request.GET.get("page")
        paginator = Paginator(queryset, 1)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
            
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        total = queryset.count()
        context.update({
            "page":page,
            "total":total,
            "query":query,
            "posts":posts,

        })

        return render(request, "blog/search_test.html", context)

def blogs(request):
    posts = Post.objects.all().filter().order_by('-id')
    page = Paginator(posts , 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'posts' : posts,
        'page' : page,
    }
    
    return render(request,'blog/blogs.html', context)

def blog(request):
    context = {}
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by('hit_count_generic')[:4]

    page = request.GET.get("page")
    paginator = Paginator(posts, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'popular_posts': popular_posts,
        'categories':categories,
        'posts': posts,
    }

    return render(request, "blog/blog.html", context)

def blog_page(request):
    return render(request, 'blog/blog.html')

class PostDetailView(HitCountDetailView):
    model = Post
    template_name = "blog/post.html"
    slug_field = "slug"
    count_hit = True

    form = CommentForm

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("post", kwargs={
                'slug': post.slug
            }))

    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context

def post_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostCreateForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('blogs')
        else:
            form = PostCreateForm()

        context = {
            'form' : form,
            }
        return render(request, 'blog/blogs_create.html', context) 
    else:
        return redirect('dashboard')

def update_blog(request, pk):
    if request.user.is_superuser:
        post=Post.objects.get(id=pk)
        form=PostCreateForm(instance=post)
        if request.method == "POST":
            form = PostCreateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('blogs')
        context = {
            "form" : form
            }
            
        return render(request, 'blog/blogs_create.html', context)
    else:
        return redirect('dashboard')

def delete_post(request, pk):
    if request.user.is_superuser:
        blog = Post.objects.get(id=pk)
        if request.method == "POST":
            blog.delete()
            return redirect('blogs') 
        context = {
            'blog': blog
            }
        return render(request, 'blog/blog_delete.html', context)
    else:
        return redirect('dashboard')

