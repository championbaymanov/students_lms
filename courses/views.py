from django.shortcuts import render, redirect
from . forms import *
from . models import *
from django.http import HttpResponse

# Create your views here.

def mentees_page(request):
    mentees = Mentee.objects.all()
    context = {
        'mentees' : mentees,
    }
    
    return render(request, 'courses/mentees_page.html', context)

def mentors_page(request):
    mentors=Mentor.objects.all()
    context = {
        'mentors' : mentors,
    }
    
    return render(request, 'courses/mentors_page.html', context)

def groups_page(request):
    groups = Group.objects.all()
    context = {
        'groups' : groups,
    }
    
    return render(request, 'courses/groups_page.html', context)
    
def courses_page(request):
    courses = Course.objects.all()
    context = {
        'courses' : courses,
    }
    
    return render(request, 'courses/courses_page.html', context)

def group_create(request):
    if request.user.is_superuser:
        form = GroupCreateForm()
        if request.method == "POST":
            form = GroupCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('groups_page')
            else:
                form = GroupCreateForm()

        context = {
            "form" : form
            }
            
        return render(request, 'courses/group_create.html', context)
    else:
        return redirect('dashboard')

def delete_group(request, pk):
    if request.user.is_superuser:
        group = Group.objects.get(id=pk)
        if request.method == "POST":
            group.delete()
            return redirect('groups_page') 
        context = {
            'group': group
            }
        return render(request, 'courses/group_delete.html', context)
    else:
        return redirect('dashboard')

def update_group(request, pk):
    if request.user.is_superuser:
        groups=Group.objects.get(id=pk)
        form=GroupCreateForm(instance=groups)
        if request.method == "POST":
            form = GroupCreateForm(request.POST, instance=groups)
            if form.is_valid():
                form.save()
                return redirect('groups_page')
        context = {
            "form" : form
            }
            
        return render(request, 'courses/group_create.html', context)
    else:
        return redirect('dashboard')

def mentor_create(request):
    if request.user.is_superuser:
        form = MentorCreateForm()
        if request.method == "POST":
            form = MentorCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mentors_page')
            else:
                form = MentorCreateForm()

        context = {
            "form" : form
            }
            
        return render(request, 'courses/mentor_create.html', context)
    else:
        return redirect('dashboard')

def delete_mentor(request, pk):
    if request.user.is_superuser:
        mentor = Mentor.objects.get(id=pk)
        if request.method == "POST":
            mentor.delete()
            return redirect('mentors_page') 
        context = {
            'mentor': mentor
            }
        return render(request, 'courses/mentor_delete.html', context)
    else:
        return redirect('dashboard')

def update_mentor(request, pk):
    if request.user.is_superuser:
        mentee=Mentor.objects.get(id=pk)
        form=MentorCreateForm(instance=mentee)
        if request.method == "POST":
            form = MentorCreateForm(request.POST, instance=mentee)
            if form.is_valid():
                form.save()
                return redirect('mentors_page')
        context = {
            "form" : form
            }
            
        return render(request, 'courses/mentor_create.html', context)
    else:
        return redirect('dashboard')

def mentee_create(request):
    if request.user.is_superuser:
        form = MenteeCreateForm()
        if request.method == "POST":
            form = MenteeCreateForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mentees_page')
            else:
                form = MenteeCreateForm()

        context = {
            "form" : form
            }
            
        return render(request, 'courses/mentee_create.html', context)
    else:
        return redirect('dashboard')

def delete_mentee(request, pk):
    if request.user.is_superuser:
        mentee = Mentee.objects.get(id=pk)
        if request.method == "POST":
            mentee.delete()
            return redirect('mentees_page') 
        context = {
            'mentee': mentee
            }
        return render(request, 'courses/mentee_delete.html', context)
    else:
        return redirect('dashboard')

def update_mentee(request, pk):
    if request.user.is_superuser:
        mentee=Mentee.objects.get(id=pk)
        form=MenteeCreateForm(instance=mentee)
        if request.method == "POST":
            form = MenteeCreateForm(request.POST, instance=mentee)
            if form.is_valid():
                form.save()
                return redirect('mentees_page')
        context = {
            "form" : form
            }
            
        return render(request, 'courses/mentee_create.html', context)
    else:
        return redirect('dashboard')

def course_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CourseCreateForm(request.POST, request.FILES)
    
            if form.is_valid():
                form.save()
                return redirect('courses_page')
        else:
            form = CourseCreateForm()

        context = {
            'form' : form,
            }
        return render(request, 'courses/course_create_test.html', context)
    else:
        return redirect('dashboard')

def update_course(request, pk):
    if request.user.is_superuser:
        course=Course.objects.get(id=pk)
        form=CourseCreateForm(instance=course)
        if request.method == "POST":
            form = CourseCreateForm(request.POST, instance=course)
            if form.is_valid():
                form.save()
                return redirect('courses_page')
        context = {
            "form" : form
            }
            
        return render(request, 'courses/course_create_test.html', context)
    else:
        return redirect('dashboard')

def delete_course(request, pk):
    if request.user.is_superuser:
        course = Course.objects.get(id=pk)
        if request.method == "POST":
            course.delete()
            return redirect('courses_page') 
        context = {
            'course': course
            }
        return render(request, 'courses/course_delete.html', context)
    else:
        return redirect('dashboard')




