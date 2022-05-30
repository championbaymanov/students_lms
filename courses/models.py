
from django.db import models

# Create your models here.

GENDER = [
    ('MALE', 'MALE'),
    ('WOMAN', 'WOMAN'),
]
class Course(models.Model):
    phota = models.ImageField(upload_to="", null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.CharField(max_length=20)
    def __str__(self):
        return self.title

class Mentor(models.Model):
    f_name = models.CharField(max_length=30)
    s_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=5, choices=GENDER, default='MALE')
    spes = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    mentor_foiz = models.PositiveIntegerField()

    def __str__(self):
        return self.f_name + ' ' + self.s_name


class Group(models.Model):
    title = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    mentee_qty = models.PositiveIntegerField()
    lesson_qty = models.PositiveIntegerField()
    mentor = models.ForeignKey(Mentor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title +' '+ 'narxi : ' + self.course.price
    
    def general_benefit(self):
        return self.course.price * self.mentee_qty

    def mentor_benefit(self):
        return (self.course.price * self.mentee_qty) * self.mentor.mentor_foiz/100

    def group_benefit(self):
        return (self.course.price * self.mentee_qty)-(self.course.price * self.mentee_qty) * self.mentor.mentor_foiz/100


class Mentee(models.Model):
    f_name = models.CharField(max_length=30)
    s_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=5, choices=GENDER, default='MALE')
    phone = models.CharField(max_length=13)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.f_name + ' ' + self.s_name
        

    