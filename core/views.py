from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse

# Create your views here.

def index(request):
    if request.method=="POST":
        roll_no = request.POST.get('roll_no') if not request.POST.get('roll_no') == "" else "null"
        return redirect(result, roll_no)
    return render(request, 'index.html')

def result(request, roll_no):
    try:
        identity = Student.objects.get(roll_no=roll_no)
        total = identity.hindi + identity.english + identity.science + identity.social_science + identity.maths + identity.computer
    except:
        return HttpResponse(f"Result of Student with roll no. {roll_no} doesn't exist. Perhaps you have entered a typo in roll no.")
    
    ctx={
        'identity':identity,
        'total':total
    }
    return render(request, 'result.html', ctx)
