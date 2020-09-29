from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from .models import appform
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def appform1(request):
    if request.method == "POST":
        picture =request.FILES.get('pic')
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        email=request.POST.get('email')
        phone_no=request.POST.get('cno')
        aadhar_number = request.POST.get('ano')
        category = request.POST.get('cat')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gen')
        mother_name = request.POST.get('mna')
        mother_job = request.POST.get('mo')
        father_name = request.POST.get('fna')
        father_phone = request.POST.get('fno')
        father_job = request.POST.get('fo')
        resident = request.POST.get('ind')
        add1 = request.POST.get('ad1')
        add2 = request.POST.get('ad2')
        country = request.POST.get('con')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pc')
        courses = request.POST.get('off')
        yours_choice = request.POST.get('specify')
        yop1 = request.POST.get('yop1')
        top1 = request.POST.get('top1')
        mop1 = request.POST.get('mop1')
        pop1 = request.POST.get('pop1')
        yop2 = request.POST.get('yop2')
        top2 = request.POST.get('top2')
        mop2 = request.POST.get('mop2')
        pop2 = request.POST.get('pop2')
        sign = request.FILES.get('sign')
        mark1 = request.FILES.get('mark1')
        mark2 = request.FILES.get('mark2')
        
        fs = FileSystemStorage()

        fs.save(picture.name, picture)
        fs.save(sign.name, sign)
        fs.save(mark1.name, mark1)
        fs.save(mark2.name, mark2)

        form_instance = appform.objects.create(picture=picture,sign=sign,mark1=mark1,mark2=mark2,first_name=first_name,last_name=last_name, email=email,phone_no=phone_no,aadhar_number=aadhar_number,category=category,date_of_birth=date_of_birth,gender=gender,mother_name=mother_name,mother_job=mother_job,father_name=father_name,father_phone=father_phone,father_job=father_job,resident=resident, add1=add1,add2=add2,country=country,state=state,city=city,pincode=pincode,courses=courses,yours_choice=yours_choice,yop1=yop1,top1=top1,mop1=mop1,pop1=pop1,yop2=yop2,top2=top2,mop2=mop2,pop2=pop2)
        form_instance.save()
        #return HttpResponse("<h3>Successfullty Registered</h3>")
        return render(request,'pay.html')

    elif request.method == "GET":
        return render(request,'form.html')       
    else:
        return redirect('/')


	

		#return render(request,'reg2.html',{'forms':form_instance})
		#return HttpResponse("<h3>Successfullty Registered</h3>")


def logout(request):
    auth.logout(request)
    return redirect('/')

def payment(request):
    return render(request,'success.html')

