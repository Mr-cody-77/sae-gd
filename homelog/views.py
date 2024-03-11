from django.shortcuts import render
from homelog.models import registered
# Create your views here.
def home(request):
    try:
        if request.method=="POST":
            name = request.POST.get("name")
            roll = request.POST.get("roll")
            dept = request.POST.get("dept")
            phone = request.POST.get("phone")
            obj = registered(name=name, roll=roll, dept = dept,phone=phone)
            obj.save()
    except Exception as e:
        pass
    return render(request, 'sae.html')
