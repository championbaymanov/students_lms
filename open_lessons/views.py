from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from open_lessons.models import *
from hitcount.views import HitCountDetailView
from open_lessons.forms import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

def searchBlog(request):
    context = {}
    posts = Open_lessons.objects.all()

    if request.method == "GET":
        query = request.GET.get("search_open_lesson")
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

        return render(request, "open_lessons/search_test.html", context)

def blogs(request):
    posts = Open_lessons.objects.all()
    page = Paginator(posts , 2)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'posts' : posts,
        'page' : page,
    }
    
    return render(request,'open_lessons/open_lessons.html', context)

class PostDetailView(HitCountDetailView):
    model = Open_lessons
    template_name = "open_lessons/open_lessons_detail.html"
    slug_field = "slug"
    count_hit = True

    form = RedisterForm

    def post(self, request, *args, **kwargs):
        form = RedisterForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()

            return redirect(reverse("open_lesson", kwargs={
                'slug': post.slug
            }))

    def get_context_data(self, **kwargs):
        post_comments_count = Register.objects.all().filter(post=self.object.id).count()
        post_comments = Register.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context

class PostDetailView_Register(HitCountDetailView):
    model = Open_lessons
    template_name = "open_lessons/table.html"
    slug_field = "slug"
    count_hit = True

    def get_context_data(self, **kwargs):
        post_comments_count = Register.objects.all().filter(post=self.object.id).count()
        post_comments = Register.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context

def open_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = OpenCreateForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('open_lesson')
        else:
            form = OpenCreateForm()

        context = {
            'form' : form,
            }
        return render(request, 'open_lessons/open_lesson_create.html', context)  
    else:
        return redirect('dashboard')

def update_open(request, pk):
    if request.user.is_superuser:
        post=Open_lessons.objects.get(id=pk)
        form=OpenCreateForm(instance=post)
        if request.method == "POST":
            form = OpenCreateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('open_lesson')
        context = {
            "form" : form
            }
            
        return render(request, 'open_lessons/open_lesson_create.html', context)
    else:
        return redirect('dashboard')

def delete_open(request, pk):
    if request.user.is_superuser:
        post = Open_lessons.objects.get(id=pk)
        if request.method == "POST":
            post.delete()
            return redirect('open_lesson') 
        context = {
            'post': post,
            }
        return render(request, 'open_lessons/open_lesson_delete.html', context)
    else:
        return redirect('dashboard')
    

