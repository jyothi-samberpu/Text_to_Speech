from django.shortcuts import render,redirect

# Create your views here.
import pyttsx3
def jyothi(request):
    return render(request,'index.html')
def vinay(request):
   value=request.GET['inp']
   obj=pyttsx3.init()
   obj.say(value)
   obj.runAndWait()
   return redirect('/')
