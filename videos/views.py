from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from videos.models import VideoContent, Category, Comments
from hitcount.views import HitCountDetailView
from videos.forms import CommentForm, VideoCreateForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

# Create your views here.

def searchBlog(request):
    context = {}
    posts = VideoContent.objects.all()

    if request.method == "GET":
        query = request.GET.get("search_videos")
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

        return render(request, "videos/search_test.html", context)

def blogs(request):
    posts = VideoContent.objects.all().filter().order_by('-id')
    page = Paginator(posts , 6)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)

    context = {
        'posts' : posts,
        'page' : page,
    }
    
    return render(request,'videos/blog.html', context)

class PostDetailView(HitCountDetailView):
    model = VideoContent
    template_name = "videos/test.html"
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

            return redirect(reverse("video", kwargs={
                'slug': post.slug
            }))

    def get_context_data(self, **kwargs):
        post_comments_count = Comments.objects.all().filter(post=self.object.id).count()
        post_comments = Comments.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })


        return context

def video_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = VideoCreateForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('videos')
        else:
            form = VideoCreateForm()

        context = {
            'form' : form,
            }
        return render(request, 'videos/video_create.html', context)  
    else:
        return redirect('dashboard')

def update_video(request, pk):
    if request.user.is_superuser:
        post=VideoContent.objects.get(id=pk)
        form=VideoCreateForm(instance=post)
        if request.method == "POST":
            form = VideoCreateForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('videos')
        context = {
            "form" : form
            }
            
        return render(request, 'videos/video_create.html', context)
    else:
        return redirect('dashboard')

def delete_video(request, pk):
    if request.user.is_superuser:
        post = VideoContent.objects.get(id=pk)
        if request.method == "POST":
            post.delete()
            return redirect('videos') 
        context = {
            'post': post
            }
        return render(request, 'videos/video_delete.html', context)
    else:
        return redirect('dashboard')




    

