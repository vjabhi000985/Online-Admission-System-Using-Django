from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class appform(models.Model):
    picture = models.FileField(upload_to='images/')
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=50)
    phone_no=models.CharField(max_length=10)
    aadhar_number = models.CharField(max_length=16)
    cat_choice = (
        ('General', 'General'),
        ('OBC', 'OBC'),
        ('ST', 'ST'),
        ('SC', 'SC'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=10, blank=True, null=True, choices=cat_choice)
    date_of_birth = models.CharField(max_length=12)
    gen_choice = (
        ('Male', 'Male'),
        ('Female','Female'),
    )
    gender = models.CharField(max_length=7, blank=True, null=True, choices=gen_choice)
    mother_name = models.CharField(max_length=120)
    mother_job = models.CharField(max_length=120)
    father_name = models.CharField(max_length=120)
    father_phone = models.CharField(max_length=120)
    father_job = models.CharField(max_length=120)
    resident = models.CharField(max_length=25)
    add1 = models.CharField(max_length=120)
    add2 = models.CharField(max_length=120)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=30)
    pincode = models.CharField(max_length=8)
    course_choice = (
        ('Undergraduate', 'Undergraduate'),
        ('Post Graduate', 'Post Graduate'),
        ('Diploma', 'Diploma'),
    )
    courses = models.CharField(max_length=25, blank=True, null=True, choices=course_choice)
    yours_choice = models.CharField(max_length=50)
    yop1 = models.CharField(max_length=4)
    top1 = models.CharField(max_length=3)
    mop1 = models.CharField(max_length=3)
    pop1 = models.CharField(max_length=3)
    yop2 = models.CharField(max_length=4)
    top2 = models.CharField(max_length=3)
    mop2 = models.CharField(max_length=3)
    pop2 = models.CharField(max_length=3)
    sign = models.FileField(upload_to='images/')
    mark1 = models.FileField(upload_to='images/')
    mark2 = models.FileField(upload_to='images/')

    def __str__(self):
        return self.first_name

# Payment model
#class pay(models.Model):
#    name=models.CharField(max_length=120)
#    card_no=models.CharField(max_length=10)
#    expiry_month=models.CharField(max_length=8)
#    expiry_year=models.CharField(max_length=4)
#    cvv=models.CharField(max_length=3)
    
    