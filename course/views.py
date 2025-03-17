from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Course

def home(request):
    course = Course.objects.all()
    return render(request, template_name="home.html",
                  context={"course":course})